from django.db import models
from datetime import datetime

class Song(models.Model):
    title = models.CharField(max_length=64)
    artist = models.CharField(max_length=128)
    audio_file = models.FileField(upload_to='song/')
    cover_image = models.FileField(blank=True, upload_to='cover/')
    cover_link = models.TextField(blank=True)
    audio_length_string = models.CharField(max_length=64)
    audio_length_second = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.utcnow)