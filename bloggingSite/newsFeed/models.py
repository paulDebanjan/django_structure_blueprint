from bloggingSite.authentication.models import User
from django.db import models



class NewsFeedImagesModel(models.Model):
    images = models.FileField(upload_to='newsFeed/', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    newsFeedID = models.CharField(max_length=50)

class NewsFeedMessageModel(models.Model):
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    newsFeedID = models.CharField(max_length=50)

