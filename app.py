import time
import os
from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/',connect=False)

db = client['db']
collection = db['test_collection']

@app.route('/v1/key/<key>', methods=['GET'])
def retrieve(key):
    result = collection.find_one({"key": key})
    return result['value']

@app.route('/v1/key/<key>/value/<value>', methods=['POST'])
def save(key,value):
    post = {'key':key,'value':value}
    post_id = collection.insert_one(post).inserted_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
