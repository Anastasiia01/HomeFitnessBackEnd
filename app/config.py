"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
print(basedir)
#load_dotenv(path.join(basedir, '.env'))

class Config:
    #Sets Flask config variables.
    FLASK_ENV = 'development'
    