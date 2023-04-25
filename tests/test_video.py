import pytest
from src.video import Video
from src.video import PLVideo


def test_video_init():
    """Тест инициализации экземпляра класса Video"""
    video = Video("123456", "Test video", "https://www.youtube.com/watch?v=123456", 1000, 50)
    assert video.video_id == "123456"
    assert video.title == "Test video"
    assert video.url == "https://www.youtube.com/watch?v=123456"
    assert video.view_count == 1000
    assert video.like_count == 50

def test_plvideo_init():
    """Тест инициализации экземпляра класса PLVideo"""
    pl_video = PLVideo("123456", "789")
    assert pl_video.video_id == "123456"
    assert pl_video.playlist_id == "789"