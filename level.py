import requests
from pymongo import MongoClient
from flask import Flask, jsonify


app = Flask(__name__)

# ------------------------------------------------------------------------------------------------------
@app.route('/level', methods=['GET'])
def get_user_level():
    client = MongoClient("mongodb+srv://admin:tong2504@cluster0.o5fzaup.mongodb.net/webteen?retryWrites=true&w=majority")
    db = client["webteen"]
    collection = db["statements"]

    all_data = collection.find()

    pipeline = [
        {"$match": {"userId": "b862595f-3ff3-420e-9ec6-fc65d7547059"}}, #FIXME change "1234" to real userId
        {
            "$group": {
                "_id": "$userId",
                "total": {"$sum": "$amount"} # change view to levels in statement collection
            }
        }
    ]

    result = list(collection.aggregate(pipeline))
    
    # Convert MongoDB result to JSON
    output = {}
    levelReader = ""
    for record in result:
        output = record['total']
    if (output < 200):
        levelReader = "Bronze"
    elif (output < 500):
        levelReader = "Silver"
    elif (output < 800):
        levelReader = "Gold"
    else:
        levelReader = "Platinum"
    
    return jsonify({'levels': levelReader})

if __name__ == '__main__':
    app.run(debug=True)
