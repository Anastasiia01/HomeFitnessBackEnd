from flask import Flask, render_template, request, redirect, url_for, session
from .datalayer import DataLayer
#import requests


app = Flask(__name__)
app.config.from_object('app.config.Config')
dataLayer = DataLayer(app.config['GOOGLE_API_KEY'])
print(dataLayer)




if __name__ == "main":
    app.run()

@app.route('/', methods=['GET','POST'])
def index():
    return "hello"
