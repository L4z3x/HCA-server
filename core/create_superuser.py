import os

from django.contrib.auth import get_user_model

MyUser = get_user_model()

ADMIN_ACCOUNT_EMAIL = os.getenv("ADMIN_ACCOUNT", "admin@c.test")
ADMIN_ACCOUNT_PASSWORD = os.getenv("ADMIN_ACCOUNT_PASSWORD", "weakpass")
ADMIN_ACCOUNT_USERNAME = os.getenv("ADMIN_ACCOUNT_USERNAME", "admin")


def create_admins(MyUser, username, email, password):
    """
    create superuser
    """
    try:
        MyUser.objects.get(email=email, username=username)
        print("===> User " + username + " already exist", flush=True)
    except MyUser.DoesNotExist:
        MyUser.objects.create_superuser(username, email, password)
        print("===> User " + username + " created with default password: " + password)


create_admins(
    MyUser, ADMIN_ACCOUNT_USERNAME, ADMIN_ACCOUNT_EMAIL, ADMIN_ACCOUNT_PASSWORD
)
