from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': "Learn Python",
        'description': "look for tutorials On Internet",
        'done': False
    },
    {
        'id': 2,
        'title': "Make Api",
        'description': "Make api from flask",
        'done': False
    },
    {
        'id': 3,
        'title': "Publish Api",
        'description': "Research about how to publish flask api on internet",
        'done': False
    }
]


@app.route("/add-data", methods=['POST'])
def add_data():
    if (not request.json):
        return jsonify({
            "Status": "Error 400",
            "Message": "Data not Provided"
        }, 400)
    task ={
        'id': tasks[-1]['id'] +1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "Status":"Sucess",
        "Message":"Task Added Sucessfully"
    })
@app.route("/get-data")
def get_data():
    return jsonify({
        "Data":tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)
