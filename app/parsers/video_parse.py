from typing import List
from youtubesearchpython import CustomSearch, VideoSortOrder
from googleapiclient.discovery import build


class YoutubeSearcher:

    def __init__(self, video_name: str, videos_number: int, comments_number: int):
        self.video_name = video_name
        self.videos_number = videos_number
        self.comments_number = comments_number
        self.video_by_views = CustomSearch(self.video_name, VideoSortOrder.viewCount, limit=videos_number)
        self.__api = 'AIzaSyAPo1tx5P0Q8NqsJSLz1APFAvHnCT9UWtQ'

    def filter_results(self) -> List:
        videos_by_vews = self.video_by_views.result()
        info_list = []
        for info in videos_by_vews['result']:
            comments = self.video_comments(info['id'], self.comments_number)
            info_dict = {
                'title': info['title'],
                'url': f"https://www.youtube.com/watch?v={info['id']}",
                'duration': info['duration'],
                'views': info['viewCount']['short'],
                'comments': comments
            }
            info_list.append(info_dict)
            
        return info_list
    
    def video_comments(self, video_id: int, comments_number: int) -> List:
        youtube = build('youtube', 'v3', developerKey=self.__api)
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=comments_number,
        )
        response = request.execute()
        comments_list = []
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            comments_list.append(comment)

        return comments_list

# searcher = YoutubeSearcher(video_name='Тестировщик', videos_number=5, comments_number=5).filter_results()
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(searcher, f, ensure_ascii=False, indent=4)