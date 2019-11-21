from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/eventList', methods=['GET', 'POST'])
def parse_request():
    data = request.get_json(silent=True, cache=False)
    if data:
        thejson = json.dumps(data)
    else:
        thejson = "no json"

    print(thejson)
    return "good job"


if __name__ == '__main__':
    app.run(debug=True)