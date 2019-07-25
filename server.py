#!/usr/bin/python3
from flask import Flask, jsonify, abort, request
from utils.tisdb import TisDb
from flask_restplus import fields, Api, Resource, cors

app = Flask(__name__)
api = Api(app, version='1.0', title='TIS API', description='A simple TIS API')
db = TisDb()

single_vector = fields.String

add_request = api.model('Add request', {
    'smartcontract': fields.String(required=True, description='The smartcontract address',
                                   example='0x644097FADEc1401F773D2407744006deEEa5C12c'),
    'phonenumber': fields.String(required=True, description='The phonenumber',
                                   example='0612345678')
})

@api.route('/get/<smartcontract>')
class GetNumber(Resource):
    @api.response(200, 'Smartcontract found.')
    @api.response(404, 'Smartcontract not found.')
    @api.doc(id='get')
    @cors.crossdomain(origin='*', headers='Content-Type, Access-Control-Allow-Headers')
    def get(self, smartcontract):
        """
            Get number for a smartcontract.
        """
        result = db.get_number(smartcontract)
        if result:
            return jsonify(smartcontract=result[0], phonenumber=result[1])
        else:
            return jsonify(), 404


@api.route('/delete/<smartcontract>')
class DeleteNumber(Resource):
    @api.response(200, 'Phonenumber successful deleted.')
    @api.doc(id='delete')
    @cors.crossdomain(origin='*', headers='Content-Type, Access-Control-Allow-Headers')
    def delete(self, smartcontract):
        """
            Delete a record based on the smartcontract address.
        """
        print("Delete contract: ", smartcontract)
        db.delete_number(smartcontract)
        return jsonify(), 200


@api.route('/add')
class AddNumber(Resource):
    @api.expect(add_request)
    @api.response(200, 'Phonenumber successfully created.')
    @api.response(400, 'Bad request.')
    @api.response(409, 'Conflict happened.')
    @api.doc(id='add')
    @cors.crossdomain(origin='*', headers='Content-Type, Access-Control-Allow-Headers')
    def post(self):
        """
            Add a new TIS record.
        """
        if not request.get_json():
            abort(400)
        content = request.get_json(force=True)
        phonenumber = content["phonenumber"]
        smartcontract = content["smartcontract"]
        result = db.add_number(smartcontract, phonenumber)

        if result == 0:
            return jsonify(), 200
        else:
            return jsonify(), 409


@api.route('/count')
class Count(Resource):
    @api.response(200, 'Number of rows.')
    @api.response(500, 'Server errors.')
    @api.doc(id='count')
    @cors.crossdomain(origin='*', headers='Content-Type, Access-Control-Allow-Headers')
    def get(self):
        """
            Count the records.
        """
        result = db.count()

        if result:
            return jsonify(records=result[0])
        else:
            return jsonify(), 500


api.add_resource(GetNumber, '/get/<smartcontract>')  # Get address
api.add_resource(AddNumber, '/add')  # Add address
api.add_resource(DeleteNumber, '/delete/<smartcontract>')  # Delete address
api.add_resource(Count, '/count')  # Search match

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
