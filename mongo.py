from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import loads, dumps


app = Flask(__name__)

client = MongoClient("mongodb://revathigeorgian:georgian123@ac-mjldwso-shard-00-00.syg45su.mongodb.net:27017,ac-mjldwso-shard-00-01.syg45su.mongodb.net:27017,ac-mjldwso-shard-00-02.syg45su.mongodb.net:27017/?ssl=true&replicaSet=atlas-dxra9k-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['test']
col = db["Collection"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/all', methods=['GET'])
def get_all_time_currencies():
    output = []

    for q in col.find():
        test = q
        del test['_id']
        output.append(test)
    print(output)
    json_str = dumps(output)
    record2 = loads(json_str)
    return record2


@app.route('/one', methods=['GET'])
def get_one_currency():
    test = col.find_one();
    del test['_id']
    print(test)
    json_str = dumps(test)
    record2 = loads(json_str)
    return record2

if __name__ == '__main__':
    app.run(debug=True)
