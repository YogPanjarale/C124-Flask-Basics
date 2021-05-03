from flask import Flask
print(__name__)
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"


if (__name__ =="__main__"):
    app.run()