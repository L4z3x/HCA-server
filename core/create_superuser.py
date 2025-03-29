import os

from django.contrib.auth import get_user_model

MyUser = get_user_model()

ADMIN_ACCOUNT = os.environ.get("ADMIN_ACCOUNT", "admin@khatamat.test")
ADMIN_ACCOUNT_PASSWORD = os.environ.get("ADMIN_ACCOUNT_PASSWORD", "weakpass")


def create_admins(MyUser, username, email, password):
    """
    create superuser
    """
    try:
        MyUser.objects.get(email=email, username=username)
        print("==> User " + username + " already exist <----- ", flush=True)
    except MyUser.DoesNotExist:
        MyUser.objects.create_superuser(username, email, password)
        print("==> User " + username + " created with default password: " + password)


create_admins(MyUser, "admin", ADMIN_ACCOUNT, ADMIN_ACCOUNT_PASSWORD)
