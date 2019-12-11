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


def make_response(result_list, one_item):
    response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "list": "0"
        }
    }

    if result_list:
        response["output"]["list"] = str(len(result_list))

        result_output = {}
        try:
            for index, result in enumerate(result_list, 1):
                for key, value in result.items():
                    if key in ['title', 'place', 'cost', 'time']:
                            if one_item:
                                result_output[key + str(index)] = value[0]
                            else:
                                result_output[key + str(index)] = value


        except Exception as e:
            print(str(e))
            print(value)

        response["output"] = dict(response["output"], **result_output)
    return response


class GetParams(Resource):
    def post(self):
        data = request.get_json()
        print(data)

        location = data['action']['parameters']['location']['value']
        ymonth = data['action']['parameters']['ymonth']['value']
        mday = data['action']['parameters']['mday']['value']

        date = makedate(ymonth, mday)

        c = content(location, date, date)

        result_list = action(c)
        response = make_response(result_list, one_item = False)

        return jsonify(response)


class GetParams1(Resource):
    def post(self):
        data = request.get_json()
        print(data)

        location = data['action']['parameters']['location']['value']
        ymonth = data['action']['parameters']['ymonth']['value']
        mday = data['action']['parameters']['mday']['value']

        date = makedate(ymonth, mday)

        c = content(location, date, date)

        result_list = action(c)
        response = make_response(result_list, one_item = True)

        return jsonify(response)


api.add_resource(GetParams, '/eventList', '/eventItem2', '/eventItem3',
                            '/2_1', '/2_2', '/3_1', '/3_2', '/3_3')

api.add_resource(GetParams1, '/eventItem1', '/yes')

if __name__ == '__main__':
    app.run(debug=True)
