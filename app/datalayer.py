"""Datalayer that will allow our server to utilize Youtube Data API"""
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class DataLayer:
    def __init__(self, key):
        self.api_key = key
        self.api_service_name = 'youtube'
        self.api_version = 'v3'
        self.youtube = build(self.api_service_name, 
                                self.api_version,
                                developerKey=self.api_key) #Resource for interacting with an API.


    def channel_search(self, channel_name):
        query= channel_name.replace(" ", "+")
        result={}
        search_response = self.youtube.search().list( # pylint: disable=maybe-no-member
            part='snippet',
            fields='items(snippet(channelId, channelTitle))',
            type='channel',
            maxResults=1,
            q=query
        ).execute()
        print(search_response)
        if (search_response['items']):
            result = search_response['items'][0]['snippet']
        return result

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


    
    
