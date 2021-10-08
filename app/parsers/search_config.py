from dataclasses import dataclass

@dataclass(frozen=True)
class SearchItems:
    views: str = 'Views'
    upload_time : str = 'Upload Time'
    rating : str = 'Rating'
