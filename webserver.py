from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/banana/<banana_id>", methods=["POST", "GET"])
def banana(banana_id):
    return "Funny banana endpoint" + banana_id
    

if __name__ == '__main__':
    app.run()