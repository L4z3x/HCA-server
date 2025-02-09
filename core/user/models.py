from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    RoleList = (
        ("admin", "admin"),
        ("user", "user"),
        ("member", "member"),
        ("writer", "writer"),
    )
    role = models.CharField(max_length=255, choices=RoleList, default="user")
