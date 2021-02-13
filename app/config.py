"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    #Sets Flask config variables.
    FLASK_ENV = 'development'
    GOOGLE_API_KEY = environ.get('GOOGLE_API_KEY') #request this API key through your own Google API Console

    