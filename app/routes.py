from flask import Flask, render_template
from flask import current_app as app

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def profile():
    return render_template('projects.html')

@app.route("/writing")
def library():
    return render_template('writing.html')
