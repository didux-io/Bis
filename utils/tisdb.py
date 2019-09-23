import os
import psycopg2
import multiprocessing

logger = multiprocessing.get_logger()
recognition_quality = 1

#  docker run --name postgres --rm -h postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d oelmekki/pg350d:9.6
db_name = os.getenv('POSTGRES_DB', 'postgres')
db_user = os.getenv('POSTGRES_USER', 'postgres')
db_password = os.getenv('POSTGRES_PASSWORD', 'mysecretpassword')
db_host = os.getenv('POSTGRES_HOST', 'localhost')
db_port = os.getenv('POSTGRES_PORT', '5432')


class DatabaseException(Exception):
    pass

class TisDb(object):
    def __init__(self):
        try:
            self.db = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        except psycopg2.Error as e:
            logger.error('Error connecting to database: {}'.format(e.pgerror))
            raise DatabaseException()
        cursor = self.db.cursor()
        self.db.commit()

        sql = """CREATE TABLE IF NOT EXISTS tis(
				id SERIAL PRIMARY KEY,
				smartcontract TEXT NOT NULL UNIQUE,
				phonenumber TEXT NOT NULL);"""
        cursor.execute(sql)
        self.db.commit()
        logger.info('TIS initialized')

    def __del__(self):
        self.db.close()

    def add_number(self, smartcontract, phonenumber):
        cursor = self.db.cursor()
        print(smartcontract)
        print(phonenumber)
        sql = """INSERT INTO tis(smartcontract, phonenumber) VALUES (%s, %s)
            ON CONFLICT(smartcontract) DO UPDATE SET phonenumber = EXCLUDED.phonenumber;"""
        data = (smartcontract, phonenumber,)
        try:
            cursor.execute(sql, data)
            self.db.commit()
        except Exception as e:
            logger.error('error adding face to database: {0}'.format(e))
            self.db.rollback()
            return -1
        if cursor.rowcount == 1:
            return 0
        else:
            return 1

    def delete_number(self, smartcontract):
        cursor = self.db.cursor()
        sql = """DELETE FROM tis WHERE smartcontract = %s"""
        data = (smartcontract,)

        cursor.execute(sql, data)
        self.db.commit()
        if cursor.rowcount == 1:
            return True
        else:
            return False

    def count(self):
        cursor = self.db.cursor()
        sql = """SELECT count(*) FROM tis;"""

        cursor.execute(sql)
        return cursor.fetchone()

    def get_number(self, phonenumber):
        cursor = self.db.cursor()
        sql = """SELECT smartcontract, phonenumber FROM tis WHERE phonenumber = %s"""
        data = (phonenumber,)

        cursor.execute(sql, data)
        return cursor.fetchone()
