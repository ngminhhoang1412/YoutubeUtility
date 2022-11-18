from googleapiclient.discovery import build
import requests
import json

class YTSearch():
    def __init__(self,api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
    
    # Get video id from url 
    def _get_video_id(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_video = dict()
        if 'items' not in data:
            return channel_video, None
        item_data = data['items']
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_video[video_id] = dict()

            except KeyError:
                print("Error")
        return channel_video
    # get results querry url from q(query search)
    def get_results_querry_url(self ,q , maxResults):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&part=id,snippet&oder=date&q={q}'
        if maxResults is not None and isinstance(maxResults , int):
            url += "&maxResults = " + str(maxResults)
        return url
    def dump(self , q , url):
        fn = q.replace(" ","_").lower()
        file_name = "Id_"+ fn + ".json"
        with open(file_name, 'a') as f:
            json.dump(self._get_video_id(url) , f ,  indent= 4)
        print("file dumped")