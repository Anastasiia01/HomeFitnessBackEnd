"""Datalayer that will allow our server to utilize Youtube Data API"""
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class DataLayer:
    def __init__(self, key):
        self.api_key = key
    
    """def __str__(self): #for debugging purposes
        return "key: " + self.api_key"""

    def video_search(self):
        """request:{
            channelId:string,
            q:string,
            maxResults:number,
            relevanceLanguage: string ("en"),
            publishedAfter:datetime ("RFC 3339 formatted date-time value (1970-01-01T00:00:00Z)"),
            type: "video"|"channel"|,
            videoDefinition: "any"|"standard"|"high",
            videoDimension: "2d",
            videoDuration: "long"|"medium",
            videoEmbeddable: "true",
        }"""
        return None


    
    
