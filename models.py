from django.db import models

class Music(models.Model):
    title = models.Charfield(max_length=120, null=True, blank=True)
    artist = models.Charfield(max_length=120, null=True, blank=True)
    album = models.Charfield(max_length=120, null=True, blank=True)
    release_date = models.DateField
    genre = models.Charfield(max_length=120, null=True, blank=True)

    def __str__(self):
        return 
