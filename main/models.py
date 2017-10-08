from django.db import models
from django.utils import timezone

# Create your models here.

class youtubeModel(models.Model):
    url = models.CharField(max_length=100, verbose_name='Url address')
    email = models.EmailField(max_length=100, verbose_name='Email')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.url