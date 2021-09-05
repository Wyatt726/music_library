from rest_framework import serializers
from models import Music 

class MusicSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, max_length=50)
    artist = serializers.CharField(required=True, allow_blank=False, max_length=100)
    album = serializers.CharField(required=True, allow_blank=False, max_length=50)
    release_date = serializers.IntegerField(allow_null=False)
    genre = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)