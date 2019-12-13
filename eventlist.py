from flask_restful import Api, Resource
from flask import Flask, jsonify, request
import datetime
from getEventList import content, action
from dbconnect import predicted_pop


app = Flask(__name__)
api = Api(app)


def makedate(ymonth, mday, has_dash):
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    if len(ymonth) == 1:
        ymonth = '0' + ymonth
    if len(mday) == 1:
        mday = '0' + mday

    if has_dash:
        date = year +'-'+ ymonth +'-'+ mday
        return date
    else:
        date = year + ymonth + mday
        return date


def translate_code(val):
    return {
        '1': '11680', '2': '11740', '3': '11305', '4': '11500', '5': '11620',
        '6': '11215', '7': '11530', '8': '11545', '9': '11350', '10': '11320',
        '11': '11230', '12': '11590', '13': '11440', '14': '11410', '15': '11650',
        '16': '11200', '17': '11290', '18': '11710', '19': '11470', '20': '11560',
        '21': '11170', '22': '11380', '23': '11110', '24': '11140', '25': '11260'
    }.get(val)


def make_response(result_list, foot_traffic, one_item):
    response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "list": "0"
        }
    }

    if len(result_list) == 0:
        return response
    
    elif len(result_list)>0:
        response["output"]["list"] = str(len(result_list))

        result_output = {}
        for index, result in enumerate(result_list, 1):
            for key, value in result.items():
                if key in ['title', 'place', 'cost', 'time']:
                        if one_item:
                            result_output[key + str(index)] = value[0]
                        else:
                            result_output[key + str(index)] = value



        response["output"] = dict(response["output"], **result_output)
        response["output"]["traffic"] = str(foot_traffic)
    return response


class GetParams(Resource):
    def post(self):
        data = request.get_json()

        location = data['action']['parameters']['location']['value']
        ymonth = data['action']['parameters']['ymonth']['value']
        mday = data['action']['parameters']['mday']['value']

        api_date = makedate(ymonth, mday, has_dash = False)
        c = content(location, api_date, api_date)

        db_date = makedate(ymonth, mday, has_dash = True)
        val = translate_code(str(location))
        
        result_list = action(c)
        foot_traffic = predicted_pop(val, str(db_date))
        
        response = make_response(result_list, foot_traffic, one_item = False)
        print(response)

        return jsonify(response)


class GetParams1(Resource):
    def post(self):
        data = request.get_json()

        location = data['action']['parameters']['location']['value']
        ymonth = data['action']['parameters']['ymonth']['value']
        mday = data['action']['parameters']['mday']['value']

        api_date = makedate(ymonth, mday, has_dash = False)
        c = content(location, api_date, api_date)

        db_date = makedate(ymonth, mday, has_dash = True)
        val = translate_code(str(location))
        
        result_list = ac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           tion(c)
        foot_traffic = predicted_pop(val, str(db_date))
        
        response = make_response(result_list, foot_traffic, one_item = True)
        print(response)

        return jsonify(response)


api.add_resource(GetParams, '/eventList', '/eventItem2', '/eventItem3',
                            '/2_1', '/2_2', '/3_1', '/3_2', '/3_3')

api.add_resource(GetParams1, '/eventItem1', '/yes')

if __name__ == '__main__':
    app.run(debug=True)
