from flask import render_template, redirect, url_for
from app import app


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    # return render_template(welcome.html)
    return "home"


@app.route('/about')
def about():
    return "about"


@app.route('/project')
def project():
    return "project"
