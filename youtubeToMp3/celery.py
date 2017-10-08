import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtubeToMp3.settings')
app = Celery('youtubeToMp3')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()