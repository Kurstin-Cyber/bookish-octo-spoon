from flask import Flask, request

app = Flask(__name__)


@app.route('/test')
def hello():
    print("Hi, the hello() function is being executed")
    return "Hello World"


app.run(port=8080)
