from flask_restful import Api, Resource, reqparse
from flask import Flask, jsonify

app = Flask(__name__)
api = Api(app)


class GetParams(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('location', type=str)
    parser.add_argument('week', type=str)
    parser.add_argument('day', type=str)

    def post(self):
        data = GetParams.parser.parse_args()

        location = data['action']['parameters']['location']['value']
        week = data['action']['parameters']['week']['value']
        day = data['action']['parameters']['day']['value']

        print({'location': location, 'week': week, 'day': day})

        response = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {
                "list": "1"
            }
        }

        return jsonify(response)


api.add_resource(GetParams, '/eventList')

if __name__ == '__main__':
    app.run(debug=True)
