from flask import Flask, render_template, url_for, request, redirect
from forms import Registration, Login
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = '701186d24e31452eb19a'

@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html', title = 'Home')


@app.route("/input_data")
def input_data():
    return render_template('input.html', title = 'Input Data Page')

@app.route("/map")
def map():
    con = sqlite3.connect("lora.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    data = cur.execute("SELECT CAST(lat AS numeric), CAST(long AS numeric) FROM  Loviragps ORDER BY timestamp DESC LIMIT 1")
    for lat, long in data:
        print lat, long
    return render_template('map.html', title = 'Map', lat = lat, long=long, data=data)

@app.route("/registration")
def registration():
    form = Registration()
    return render_template('registration.html', title = 'Registration', form = form)

@app.route("/login")
def login():
    form = Login()
    return render_template('login.html', title = 'Login', form = form)

if __name__=='__main__':
    app.run(debug=True)
