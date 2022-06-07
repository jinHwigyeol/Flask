#!/usr/bin/python3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.errorhandler(404)
def error_404(error):
    return "<H1> Sorry, File Not Found!</H1>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_form')
def login():
    return render_template('login_form.html')

@app.route('/login', methods = ['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['passwd']
        return render_template('reply.html', name=user,passwd=password)

    else:
        user = request.args['name']
        password = request.args['passwd']
        return render_template('reply.html', name=user,passwd=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)