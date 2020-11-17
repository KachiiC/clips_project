import json
from flashcards.models import YoutubeClip


def create_new_youtube_clip(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)
        for item in data["items"]:
            YoutubeClip(
                youtube_id=item["snippet"]["resourceId"]["videoId"],
            ).save()
