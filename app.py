import time
import os
from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27000/',connect=False)

db = client['db']
collection = db['test_collection']

@app.route('/v1/key/<key>', methods=['GET'])
def retrieve(key):
    result = collection.find_one({"key": key})
    return result['value']

@app.route('/v1', methods=['POST'])
def save():
    if request.method == 'POST':
        data = request.data.decode('ascii')
        items = data.split('&')
        post = {}
        for item in items:
            pair = item.split('=')
            post[pair[0]] = pair[1]
        post_id = collection.insert_one(post).inserted_id
        return 'successfully save'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
