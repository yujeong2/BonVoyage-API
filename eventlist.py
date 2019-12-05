from flask_restful import Api, Resource
from flask import Flask, jsonify, request
import datetime
from getEventList import content, action

app = Flask(__name__)
api = Api(app)


def makedate(ymonth, mday):
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    if len(ymonth) == 1:
        ymonth = '0' + ymonth
    if len(mday) == 1:
        mday = '0' + mday
    date = year + ymonth + mday
    return date

def makeResponse(resultList):
    listLength = len(resultList)

    if listLength == 0:
        response = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {
                    "list": 0
            }
        }
        return response

    elif listLength == 1:
        response = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {
                "list": 1,
                "title": resultList[0].get('title'),
                "place": resultList[0].get('place'),
                "cost": resultList[0].get('cost'),
                "time": resultList[0].get('time')
            }
        }
        return response


class GetParams(Resource):

    def post(self):
        data = request.get_json()

        location = data['action']['parameters']['location']['value']
        ymonth = data['action']['parameters']['ymonth']['value']
        mday = data['action']['parameters']['mday']['value']

        date = makedate(ymonth, mday)

        c = content(location, date, date)
        resultList = action(c)
        response = makeResponse(resultList)

        print(response)
        return jsonify(response)


api.add_resource(GetParams, '/eventList')


if __name__ == '__main__':
    app.run(debug=True)
