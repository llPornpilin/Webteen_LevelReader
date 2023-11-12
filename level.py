from pymongo import MongoClient
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/levels', methods=['GET'])

def get_book_views():
    client = MongoClient("mongodb+srv://admin:tong2504@cluster0.o5fzaup.mongodb.net/webteen?retryWrites=true&w=majority")
    db = client["webteen"]
    collection = db["Book"]

    all_data = collection.find()

    pipeline = [
        {
            "$group": {
                "_id": "$userId",
                "total": {"$sum": "$view"} # change view to levels in statement collection
            }
        }
    ]

    result = list(collection.aggregate(pipeline))
    
    # Convert MongoDB result to JSON
    output = {}
    for record in result:
        output = record['total']
    
    return jsonify({'levels': output})

if __name__ == '__main__':
    app.run(debug=True)
