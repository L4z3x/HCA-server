from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("user", "User"),
    ("writer", "Writer"),
    ("admin", "Admin"),
)

DEPARTEMENT_CHOICES = (
    ("logistic", "logistic"),
    ("media", "media"),
    ("management", "management"),
    ("other", "other"),
)


class user(AbstractUser):
    score = models.IntegerField(default=0)
    profilePic = models.ImageField(
        upload_to="profile_pics/", default="profile_pics/default.jpg"
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    departement = models.CharField(
        max_length=20, choices=DEPARTEMENT_CHOICES, default="other"
    )
