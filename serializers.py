from rest_framework import serializers
from models import Music 

class MusicSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, max_length=50)
    artist = serializers.CharField(required=True, allow_blank=False, max_length=100)
    album = serializers.CharField(required=True, allow_blank=False, max_length=50)
    release_date = serializers.IntegerField(allow_null=False)
    genre = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def create(self, validated_data):
        return Music.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.genre = validated_data.get('genre', instance)