import os
import psycopg2
import multiprocessing

logger = multiprocessing.get_logger()
recognition_quality = 1

#  docker run --name postgres --rm -h postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d diduxio/pg512d:latest
db_name = os.getenv('POSTGRES_DB', 'postgres')
db_user = os.getenv('POSTGRES_USER', 'postgres')
db_password = os.getenv('POSTGRES_PASSWORD', 'mysecretpassword')
db_host = os.getenv('POSTGRES_HOST', 'localhost')
db_port = os.getenv('POSTGRES_PORT', '5432')


class DatabaseException(Exception):
    pass


# Compute a confidence score based on the distance between the face vectors
def distance_to_score(distance):
    score = 1 - distance
    score = abs(score * 100)
    score += 20
    # score = abs(round(int(distance)*100)) + 20
    if score > 100:
        score = 100
    return int(score)


class BisDb(object):
    def __init__(self):
        try:
            self.db = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        except psycopg2.Error as e:
            logger.error('Error connecting to database: {}'.format(e.pgerror))
            raise DatabaseException()
        cursor = self.db.cursor()
        sql = """CREATE EXTENSION IF NOT EXISTS cube"""
        cursor.execute(sql)
        self.db.commit()

        sql = """CREATE TABLE IF NOT EXISTS bis(
				id SERIAL PRIMARY KEY,
				smartcontract TEXT NOT NULL UNIQUE,
				organisation TEXT NOT NULL,
				model_name VARCHAR(16),
				model_version VARCHAR(8),
				face_vector cube NULL);
                CREATE INDEX IF NOT EXISTS bis_organisation_index ON bis(organisation, model_name, model_version);
                """
        cursor.execute(sql)
        self.db.commit()
        logger.info('BIS initialized')

    def __del__(self):
        self.db.close()

    def add_contract(self, smartcontract, organisation, model_name, model_version, face_vector):
        cursor = self.db.cursor()
        sql = """INSERT INTO bis(smartcontract, organisation, model_name, model_version, face_vector) VALUES (%s, %s, %s, %s, CUBE(array[{}]))
            ON CONFLICT(smartcontract) DO UPDATE SET (organisation, model_name, model_version, face_vector) = (EXCLUDED.organisation, EXCLUDED.model_name, EXCLUDED.model_version, EXCLUDED.face_vector);""".format(
            ','.join(str(s) for s in face_vector))
        data = (smartcontract, organisation, model_name, model_version,)
        try:
            cursor.execute(sql, data)
            self.db.commit()
        except Exception as e:
            logger.error('error adding contract to database: {0}'.format(e))
            self.db.rollback()
            return -1
        if cursor.rowcount == 1:
            return 0
        else:
            return 1

    def delete_contract(self, smartcontract):
        cursor = self.db.cursor()
        sql = """DELETE FROM bis WHERE smartcontract = %s"""
        data = (smartcontract,)

        cursor.execute(sql, data)
        self.db.commit()
        if cursor.rowcount == 1:
            return True
        else:
            return False

    def count(self):
        cursor = self.db.cursor()
        sql = """SELECT count(*) FROM bis;"""

        cursor.execute(sql)
        return cursor.fetchone()

    def countByOrganisaton(self, organisation):
        cursor = self.db.cursor()
        sql = """SELECT count(*) FROM bis WHERE organisation = %s;"""
        data = organisation

        cursor.execute(sql, data)
        return cursor.fetchone()

    def get_contract(self, smartcontract):
        cursor = self.db.cursor()
        sql = """SELECT smartcontract, organisation, model_name, model_version FROM bis WHERE smartcontract = %s"""
        data = (smartcontract,)

        cursor.execute(sql, data)
        return cursor.fetchone()

    def find_match(self, face_vector, organisation, model_name, model_version):
        cursor = self.db.cursor()
        sql = """SELECT smartcontract, organisation, model_name, model_version, sqrt(power(CUBE(array[{0}]) <-> face_vector, 10))
        			FROM bis WHERE organisation = %s AND model_name = %s AND model_version = %s AND sqrt(power(CUBE(array[{0}]) <-> face_vector, 10)) <= {1}""" \
                  .format(','.join(str(s) for s in face_vector), recognition_quality) + \
              """ ORDER BY sqrt(power(CUBE(array[{0}]) <-> face_vector, 10)) ASC LIMIT 1""" \
                  .format(','.join(str(s) for s in face_vector))
        data = (organisation, model_name, model_version,)

        cursor.execute(sql, data)
        all_rows = cursor.fetchall()
        if all_rows:
            return all_rows[0]

        return None

    def find_matches(self, face_vector):
        cursor = self.db.cursor()
        sql = """SELECT smartcontract, sqrt(power(CUBE(array[{0}]) <-> face_vector, 2))
			FROM bis WHERE sqrt(power(CUBE(array[{0}]) <-> face_vector, 2)) <= {1}""" \
                  .format(','.join(str(s) for s in face_vector), recognition_quality) + \
              """ ORDER BY sqrt(power(CUBE(array[{}]) <-> face_vector, 2)) ASC""" \
                  .format(','.join(str(s) for s in face_vector))

        cursor.execute(sql)
        all_rows = cursor.fetchall()

        matches = []
        for row in all_rows:
            matches.append({'id': row[0], 'confidence': distance_to_score(row[1])})

        return matches
