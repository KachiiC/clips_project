from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import YoutubeClip
from .serializers import YoutubeClipSerializer

@api_view(['GET'])
def youtube_clip_list(request):
        data = YoutubeClip.objects.all()

        serializer = YoutubeClipSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def single_youtube_clip(request, youtube_id):
    try:
        playlist = YoutubeClip.objects.get(youtube_id=youtube_id)
    except YoutubeClip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = YoutubeClipSerializer(playlist, context={'request': request})

    return Response(serializer.data)

@api_view(['PUT'])
def edit_youtube_clips:
    serializer = ExampleSerializer(example, data=request.data, context={'request': request}, )

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        example.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)