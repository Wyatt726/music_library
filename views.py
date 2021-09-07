from http.client import SERVICE_UNAVAILABLE
from django.shortcuts import render
from django.http import HttpResponse, request
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response, responses

def get(self, rewuest):
    music = Music.objects.all()
    serializer = MusicSerialization(music, many = True)
    return Response(serializer.data)

def post(self, request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response(serializer.data, status=status.HTTP_201_CREATED)
    return response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
class MusicDetail(APIView):
    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk):
            music = self.get_object(pk)
            music.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
