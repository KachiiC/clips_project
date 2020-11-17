from rest_framework import serializers
from .models import YoutubeClip


class YoutubeClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeClip
        fields = ('youtube_id', 'start_stamp', 'end_stamp')