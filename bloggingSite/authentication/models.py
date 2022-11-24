from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)