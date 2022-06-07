#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def welcome():
    return "<h1> Welcome to the MTE world </h1>"

@app.route('/hello')
def hello():
    return "<h1>Hello MTE</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)