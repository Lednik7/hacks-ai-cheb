from flask import Flask
from flask import request
from flask import json,Response
from pickle import load
import flask


app = Flask(__name__)



@app.route('/hackai', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        f = open('base.txt.', 'r')
        r = f.read()
        f.close()
        s = request.form['address'] + ',' + request.form['name'] + ',' + request.form['email'] + ',' + request.form['text']
        f = open('base.txt', 'w')
        f.write(r + ';' + s)
        f.close()
        return {'post' : 'True'}
    else:
        return flask.render_template('service3.html')
app.run(host='0.0.0.0')