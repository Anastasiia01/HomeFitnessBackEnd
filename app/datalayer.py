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
        query = channel_name.replace(" ", "+")
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

    def get_video_duration(self, video_id):
        return 10

    def video_search(self, channel_id, query, mins):
        """ publishedAfter:datetime ("RFC 3339 formatted date-time value (1970-01-01T00:00:00Z)"),
            videoDefinition: "any"|"standard"|"high",
        """
        if not channel_id:
            channel_id ='UChVRfsT_ASBZk10o0An7Ucg'
        query = query.replace(" ", "+")
        if(mins>20):
            duration='long'
        else:
            duration='medium'
        search_response = self.youtube.search().list( # pylint: disable=maybe-no-member
            channelId=channel_id,
            fields='items(id(videoId), snippet(title))',        
            maxResults=5,
            part='id, snippet',
            q=query,
            relevanceLanguage='en',
            type='video',
            videoDefinition='high',
            videoDimension='2d',
            videoDuration=duration,
            videoEmbeddable = 'true'
        ).execute()
        print(search_response)
        """if (search_response['items']):
            for video in search_response['items']:
                print(video) #for debugging
                video_id = video['id']['videoId']
                dur=self.get_video_duration(video_id)
                if abs(dur-mins)<5:
                    return video"""
        return search_response



  
    
