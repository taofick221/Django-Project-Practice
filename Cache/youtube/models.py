from django.db import models

class YoutubeUser(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    subscribe=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    