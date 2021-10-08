from app.parsers.search_config import SearchItems

from typing import Union

from youtubesearchpython import CustomSearch, VideoSortOrder
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class YoutubeSearcher:

    def __init__(self, video_name: str, videos_number: int, comments_number: int, search_by=None):
        self.video_name = video_name
        self.videos_number = videos_number
        self.comments_number = comments_number
        self.search_by = search_by
        self.video_by_views = CustomSearch(self.video_name, VideoSortOrder.viewCount, limit=videos_number)
        self.video_by_rating = CustomSearch(self.video_name, VideoSortOrder.rating, limit=videos_number)
        self.video_by_upload_date = CustomSearch(self.video_name, VideoSortOrder.uploadDate, limit=videos_number)
        self.__api = 'AIzaSyAPo1tx5P0Q8NqsJSLz1APFAvHnCT9UWtQ'

    def filter_results(self) -> list:
        if self.search_by == SearchItems.views:
            videos_by_vews = self.video_by_views.result()
            return self.parse_result(videos_by_vews)
        elif self.search_by == SearchItems.rating:
            videos_by_rating = self.video_by_rating.result()
            return self.parse_result(videos_by_rating)
        elif self.search_by == SearchItems.upload_time:
            videos_by_upload_time = self.video_by_upload_date.result() 
            return self.parse_result(videos_by_upload_time)       

    def parse_result(self, by_term):
        info_list = []
        for info in by_term['result']:
            comments = self.video_comments(info['id'], self.comments_number)
            info_dict = {
                'title': info['title'],
                'url': f"https://www.youtube.com/watch?v={info['id']}",
                'duration': info['duration'],
                'views': info['viewCount']['short'],
                'comments': 'Comments are disabled' if comments is None else comments
            }
            info_list.append(info_dict)

        return info_list
    
    def video_comments(self, video_id: int, comments_number: int) -> Union[list, str]:
        youtube = build('youtube', 'v3', developerKey=self.__api)
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=comments_number,
        )
        comments_list = []
        try:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
                comments_list.append(comment)
        except HttpError:
            comments_list = None
        return comments_list


# DEBUGGING
# searcher = YoutubeSearcher(video_name='Тестировщик', videos_number=5, comments_number=5, search_by='Upload Time').filter_results()
# with open('upload.json', 'w', encoding='utf-8') as f:
#     json.dump(searcher, f, ensure_ascii=False, indent=4)