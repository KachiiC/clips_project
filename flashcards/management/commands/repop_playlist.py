from django.core.management.base import BaseCommand
import os
# Models
from flashcards.models import YoutubeClip
from flashcards.management.commands.repoppers_playlist import create_new_youtube_clip

YOUTUBE_DATA_DIR = os.getcwd() + "/flashcards/data/"

# place your data here
repop_data = ["ufcFightsData.json"]


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Deletes all Videos/Playlists and repopulates them the the prep_youtube data"""
        YoutubeClip.objects.all().delete()

        for file in repop_data:
            create_new_youtube_clip(YOUTUBE_DATA_DIR + file)
            print(f"successfully added {file}")

        print("successfully new playlists")
        print("Repop complete!")
