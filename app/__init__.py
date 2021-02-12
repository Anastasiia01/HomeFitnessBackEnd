from flask import Flask, render_template, request, redirect, url_for, session
#import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6f0cc646e644b15d920872d4d2756d480e455f447124405'
app.config['DEBUG'] = True


if __name__ == "main":
    app.run()

@app.route('/', methods=['POST'])
def index():
    return "hello"
