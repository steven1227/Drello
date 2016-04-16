# all the imports
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
   

# email: email, password: password

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    # todo database 
    json_data = request.json
    if json_data['email'] == 'rendong_liu@hotmail.com' and json_data['password']==123:
        session['loggedin'] = True
        status = True
    else:
        status = False
    return   jsonify({'result':status})  

@app.route('/api/logout')
def logout():
    session.pop('loggedin', None)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run()




