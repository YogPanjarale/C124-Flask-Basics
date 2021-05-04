from flask import Flask,request,jsonify

app = Flask(__name__)

contacts=[
    {
        "Contact":"99876444560",
        "Name": "Raju",
        "done":False,
        "id":1
    },
    {
        "Contact":"9876543222",
        "Name": "Rahul",
        "done":False,
        "id":2
    },
]

@app.route("/add-data",methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            "Status": "Error 400",
            "Message": "Data not Provided"
        }, 400)
    contact ={
        'id': contacts[-1]['id'] +1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "Status":"Sucess",
        "Message":"Task Added Sucessfully"
    })
    pass