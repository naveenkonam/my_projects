# Coding for blog

# importing modules
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return render_template("home.html") 

