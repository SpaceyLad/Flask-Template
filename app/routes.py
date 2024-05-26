from flask import render_template
from app import app
import config as conf

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/alert')
def alert():
    return render_template('alert.html')


@app.route('/fancy')
def hello_world_fancy():
    return render_template('fancy.html')


@app.route('/secret')
def secret():
    secret_key = conf.Secrets.SECRET_KEY
    return render_template('secret.html', secret_key=secret_key)