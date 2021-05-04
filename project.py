from flask import Flask

app = Flask(__name__)

conacts=[
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