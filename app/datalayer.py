"""Datalayer that will allow our server to utilize Youtube Data API"""
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class DataLayer:
    def __init__(self, key):
        self.api_key = key
    
    def __str__(self):
        return "key: " + self.api_key

    
    
