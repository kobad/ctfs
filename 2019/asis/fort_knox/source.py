from flask import Flask, session
from flask_session import Session
from flask import request
from flask import render_template
from jinja2 import Template

import fort

Flask.secret_key = fort.SECKEY

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Session(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/ask", methods = ["POST"])
def ask():
    question = request.form["q"]
    for c in "._%":
        if c in question:
            return render_template("no.html", err = "no " + c)
    try:
        t = Template(question)
        t.globals = {}
        answer = t.render({
            "history": fort.history(),
            "credit": fort.credit(),
            "trustworthy": fort.trustworthy()
        })
    except:
        return render_template("no.html", err = "bad")
    return render_template("yes.html", answer = answer)

@app.route("/door/<door>")
def door(door):
    if fort.trustworthy():
        return render_template("flag.html", flag = fort.FLAG)
    doorNum = 0
    if door is not None:
        doorNum = int(door)
    if doorNum > 0 and doorNum < 7:
        fort.visit(doorNum)
        return render_template("door.html", door = doorNum)
    return render_template("no.html", err = "Door not found!")
