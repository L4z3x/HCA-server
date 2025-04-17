from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-s4r7za-8fuu%vfr$(ra!1!lo5wb8a6a=a3vd@0w(6en9w%pudz"

DEBUG = True

LANGUAGE_CODE = "en-us"

AUTH_USER_MODEL = "user.user"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TOKEN_MODEL = None


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # cors headers:
    "corsheaders",
    # drf packages:
    "rest_framework",
    "drf_spectacular",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    # auth:
    "django.contrib.sites",
    "allauth",
    "dj_rest_auth.registration",
    "allauth.account",
    # local apps:
    "user",
    "blog",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOWS_CREDENTIALS = True

BASE_URL = "http://localhost:8000"

ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

REST_USE_JWT = True

SITE_ID = 1

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "access_token",
    "JWT_AUTH_REFRESH_COOKIE": "refresh_token",
    "JWT_AUTH_REFRESH_COOKIE_PATH": "/auth/token/get-refresh/",
    "TOKEN_MODEL": None,
    "OLD_PASSWORD_FIELD_ENABLED": True,
    "JWT_AUTH_HTTPONLY": False,  # enable this to allow javascript to access the cookie (refresh token)
    """    
    there is a problem with the httponly flag,
    it will associate every request with that cookie
    and that will raise an error in simplejwt, so we need to disable it for now  
    we must not send access_tokens (cookie) in requests to the allowAny endpoints e.g. login
    https://forum.djangoproject.com/t/solved-allowany-override-does-not-work-on-apiview/9754
    """
    "JWT_AUTH_SECURE": not DEBUG,  # False for development
    "JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED": not DEBUG,  # False for developement
    "USER_DETAILS_SERIALIZER": "user.serializers.UserSerializer",
    # "REGISTER_SERIALIZER": "khatamat_b.serializers.CustomRegisterSerializer",
}

SPECTACULAR_SETTINGS = {
    """
     In production, we should secure the docs endpoint by changing the permission class
    from AllowAny to IsAdminUser (cutom permission for site admins). This ensures that only admin users can access the documentation. 
    """
    "TITLE": "HCA",
    "DESCRIPTION": "HCA API documentation",
    "OPERATION_ID_GENERATOR": "drf_spectacular.utils.simple_operation_id_generator",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.AllowAny"
    ],  # change to IsAdminUser in prod
    "SERVE_URLCONF": "core.urls",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=100
    ),  # TODO: change to 15 minutes in production
    "REFRESH_TOKEN_LIFETIME": timedelta(days=20),
    "ROTATE_REFRESH_TOKENS": True,  # automatically rotate refresh tokens
    "BLACKLIST_AFTER_ROTATION": True,  # old refresh tokens will be blacklisted
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
}

CSRF_COOKIE_SECURE = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Email backend configuration for local development
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"  # Directory to store sent emails

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
