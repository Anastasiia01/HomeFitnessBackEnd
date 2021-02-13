from flask import Flask, render_template, request, redirect, url_for, session
from .datalayer import DataLayer
#import requests


app = Flask(__name__)
app.config.from_object('app.config.Config')
dataLayer = DataLayer(app.config['GOOGLE_API_KEY'])

if __name__ == "main":
    app.run()

@app.route('/channel', methods=['POST'])
def get_channel_id():
    """
    Receives query with json obj that contains a single  key:
        channel_name: str
    Returns channel ID.
    """

@app.route('/video', methods=['POST'])
def get_video():
    """
    Receives query with the json object and returns link to the most suitable video.
    Format of input JSON obj:
        channel_id: str 
        workout_type: str[] (e.g. [body_part, cardio])
        mins: int  (then used for videoDuration: "long"|"medium")  
    """

    request_data = request.get_json() #get parameters from request

    channel_id = None

    if request_data:
        if 'channel_id' in request_data:
            channel_id = request_data['channel_id']
    return "The Youtube channel ID is: {}".format(channel_id)
