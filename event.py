from flask import Flask, request, jsonify
import json

app = Flask(__name__)

response = {
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "title": "123"
    }
}

@app.route('/eventList', methods=['GET', 'POST'])
def parse_request():
    data = request.get_json(silent=True, cache=False)
    if data:
        thejson = json.dumps(data)
    else:
        thejson = "no json"

    print(thejson)

    return jsonify(response), jsonify(thejson)

if __name__ == '__main__':
    app.run(debug=True)