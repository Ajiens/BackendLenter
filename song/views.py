from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Song
from .serializers import SongSerializer

class SongData(APIView):
    serializer_class = SongSerializer

    def get(self, request, id=None, *args, **kwargs):
        if id is not None:
            # Retrieve a single Song instance based on the provided ID
            song = get_object_or_404(Song, id=id)
            # Serialize the song instance
            serializer = self.serializer_class(song)
            serialized_song_data = serializer.data
            # You can access additional fields and customize the response as needed
        else:
            # Retrieve all Song instances from the database
            songs = Song.objects.all()
            # Serialize all songs
            serializer = self.serializer_class(songs, many=True)
            serialized_song_data = serializer.data

        # return HttpResponse(ser.serialize("json", songs), content_type="application/json")
        return Response(serialized_song_data)
