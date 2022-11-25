from django.db import models


class NewsFeedModel(models.Model):
    message = models.TextField()
    images = models.FileField()
