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
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None
        self.update_channel_info()


    # def print_info(self, channel_id) -> None:
    #     """Выводит в консоль информацию о канале."""
    #     channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    #     print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def update_channel_info(self):
        """Обновляет информацию о канале из YouTube API"""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_info = channel['items'][0]
        self.title = channel_info['snippet']['title']
        self.description = channel_info['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(channel_info['statistics']['subscriberCount'])
        self.video_count = int(channel_info['statistics']['videoCount'])
        self.view_count = int(channel_info['statistics']['viewCount'])

    def to_json(self, filename: str):
        """Сохраняет значения атрибутов экземпляра Channel в файл в формате JSON"""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'link': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def __str__(self):
        """Возвращает строковое представление объекта Channel"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Оператор сложения для суммирования количества подписчиков двух каналов"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Оператор вычитания для разности количества подписчиков двух каналов"""
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        """Оператор меньше для сравнения количества подписчиков двух каналов"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """Оператор меньше или равно для сравнения количества подписчиков двух каналов"""
        return self.subscriber_count <= other.subscriber_count