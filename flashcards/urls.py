from django.urls import path
from . import views

urlpatterns = [
    path('youtube_clips/', views.youtube_clip_list, name="youtube_clips"),
    path('youtube_clip/<str:youtube_id>', views.single_youtube_clip, name="single_youtube_clip")
]

