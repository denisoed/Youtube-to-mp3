import os
import youtube_dl
import ffmpy
from youtubeToMp3.celery import app

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'main/static')

@app.task
def handler_youtube_video(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(STATIC_DIR, 'video/%(id)s.%(ext)s')
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url)
        video_id = video_info.get('id', None)
        video_format = video_info.get('ext', None)

    handler_ffmpy(video_id)


def handler_ffmpy(name):
    ff = ffmpy.FFmpeg(
        inputs={'%s/video/%s.webm' % (STATIC_DIR, name): None},
        outputs={'%s/audio/%s.mp3' % (STATIC_DIR, name): '-b:a 128k'}
    )

    ff.run()


def send_to_email():
    pass
