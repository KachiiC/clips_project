from django.db import models


class YoutubeClip(models.Model):
    youtube_id = models.CharField("id", max_length=100)
    start_stamp = models.IntegerField(blank=True, null=True)
    end_stamp = models.IntegerField(blank=True, null=True)
