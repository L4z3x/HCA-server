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


def rename_upload(
    instance,
    filename,
):
    ext = filename.split(".")[-1]
    folder = (
        "profile-pics"
        if instance.__class__.__name__.lower() == "user"
        else "blog-thumbnails"
        if instance.__class__.__name__.lower() == "blog"
        else "other"  # default folder
    )

    return f"{folder}/{instance.id}.{ext}"


class user(AbstractUser):
    score = models.IntegerField(default=0)
    profilePic = models.URLField(null=True)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    departement = models.CharField(
        max_length=20, choices=DEPARTEMENT_CHOICES, default="other"
    )
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
