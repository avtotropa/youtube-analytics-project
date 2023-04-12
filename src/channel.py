import os
import json

from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.environ.get('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self, channel_id) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

