from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    score = models.IntegerField(default=0)
    profilePic = models.ImageField(
        upload_to="profile_pics/", default="profile_pics/default.jpg"
    )
