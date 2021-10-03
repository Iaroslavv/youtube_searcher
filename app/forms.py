from googleapiclient.discovery import build


api = 'AIzaSyAPo1tx5P0Q8NqsJSLz1APFAvHnCT9UWtQ'


def video_comments(video_id, comments_number):
    
    youtube = build('youtube', 'v3',
                    developerKey=api)

    request = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    maxResults=comments_number,
    )
    response = request.execute()
    new_list = []
    for i in response['items']:
        just = i['snippet']['topLevelComment']['snippet']['textOriginal']
        new_list.append(just)
    return new_list
        
    
        
print(video_comments('YGiUEkbKubk', 3))