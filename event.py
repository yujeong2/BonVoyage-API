from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/eventList', methods=['POST'])
def JsonHandler():
    print (request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON Posted'

if __name__ == '__main__':
    app.run(debug=True)