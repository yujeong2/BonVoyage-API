from flask import Flask, jsonify
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

response = {
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "list": "0"
    }
}

class MakeResponse(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('location', type=str)
            parser.add_argument('week', type=str)
            parser.add_argument('day', type=str)
            args = parser.parse_args()

            _Location = args['location']
            _Week = args['week']
            _Day = args['day']

            output = {
                "list": 0,
                "location": _Location,
                "week": _Week,
                "day": _Day
            }

            response['output']= output

            return jsonify(response)

api.add_resource(MakeResponse, '/eventList')

if __name__ == '__main__':
    app.run(debug=True)