from flask_restful import Api, Resource
from flask import Flask, jsonify, request
import datetime


app = Flask(__name__)
api = Api(app)


def makedate(ymonth, mday):
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    date = year + ymonth + mday
    return date

class GetParams(Resource):

    def post(self):
        data = request.get_json()

        location = data['action']['parameters']['location']['value']
        ymonth = data['action']['parameters']['ymonth']['value']
        mday = data['action']['parameters']['mday']['value']

        date = makedate(ymonth, mday)

        print({'location': location, 'ymonth': ymonth, 'mday': mday, 'date': date})

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
