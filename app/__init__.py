from flask import Flask, render_template, request, redirect, url_for, session
from .datalayer import DataLayer
#import requests


app = Flask(__name__)
app.config.from_object('app.config.Config')
dataLayer = DataLayer(app.config['GOOGLE_API_KEY'])
print(dataLayer)




if __name__ == "main":
    app.run()

@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json() #get parameters from request
    channel_id = request_data['channel_id']
    return "The Youtube channel ID is: {}".format(channel_id)
