from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from flashcards.models import YoutubeClip
from flashcards.serializers import YoutubeClipSerializer


class YoutubeVideosTest(APITestCase):
    endpoint = reverse('youtube_clips')

    youtube_video_1 = YoutubeClip(
        youtube_id="kyhgMr0J36o",
    )

    youtube_video_2 = YoutubeClip(
        youtube_id="MyI8AsqLWPI",
    )

    expected_videos = [youtube_video_1, youtube_video_2]

    def setUp(self):
        for obj in self.expected_videos:
            obj.save()

    def test_retrieve_all_clips(self):
        """"Retrieve all clips"""
        serializer = YoutubeClipSerializer(self.expected_videos, many=True)

        response = self.client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_retrieve_single_clip(self):
        """"Retrieve single clips"""
        single_clip = reverse('single_youtube_clip', args=[self.youtube_video_1.youtube_id])

        clip = YoutubeClip.objects.get(youtube_id=self.youtube_video_1.youtube_id)

        serializer = YoutubeClipSerializer(clip)

        response = self.client.get(single_clip)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

