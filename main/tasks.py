import os
import youtube_dl
import ffmpy
from youtubeToMp3.celery import app
from django.core.mail import  EmailMessage
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'main/static')

@app.task
def handler_youtube_video(url, user_email):

    uuid_audio_title = str(uuid.uuid4())
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(STATIC_DIR, 'video/%(id)s.%(ext)s')
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url)
        video_title = video_info.get('title', None)
        video_id = video_info.get('id', None)
        video_format = video_info.get('ext', None)

    # Start convert video to mp3
    handler_ffmpy(video_id, uuid_audio_title)

    # Send email
    send_to_email(video_title, user_email, uuid_audio_title)


def handler_ffmpy(name, uuid_title):

    ff = ffmpy.FFmpeg(
        inputs={'%s/video/%s.webm' % (STATIC_DIR, name): None},
        outputs={'%s/audio/%s.mp3' % (STATIC_DIR, uuid_title): '-b:a 128k'}
    )
    ff.run()


def send_to_email(video_title, user_email, uuid_title):

    email_content = EmailMessage('Youtube To Mp3', '%s' % video_title, 'denisod93@gmail.com', [user_email])

    email_content.attach_file('%s/audio/%s.mp3' % (STATIC_DIR, uuid_title))
    email_content.send()
