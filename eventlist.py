from flask_restful import Api, Resource
from flask import Flask, jsonify, request

app = Flask(__name__)
api = Api(app)


class GetParams(Resource):

    def post(self):
        data = request.get_json()

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
