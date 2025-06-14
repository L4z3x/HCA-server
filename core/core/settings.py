from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import dj_database_url

load_dotenv("../app.env")
load_dotenv()
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-s4r7za-8fuu%vfr$(ra!1!lo5wb8a6a=a3vd@0w(6en9w%pudz"
)


DEBUG = os.environ.get("DEBUG", "True").lower() in ("true", "1", "yes")

LANGUAGE_CODE = "en-us"

AUTH_USER_MODEL = "user.user"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

PROD = os.environ.get("PROD", "False").lower() in ("true", "1", "yes")

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
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "dj_rest_auth",
    # local apps:
    "user",
    "feedback",
    "blog",
]
# ===== CORS and CSRF settings =====
if not PROD:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        os.environ.get("FRONTEND_URL", "http://localhost:3000"),
    ]
    CORS_ALLOWED_ORIGINS = [
        os.environ.get("FRONTEND_URL", "http://localhost:3000"),
    ]

CORS_ALLOWS_CREDENTIALS = True

ALLOWED_HOSTS = ["*"]

CSRF_COOKIE_SECURE = True if not DEBUG else False


# ==== Django REST Framework settings ====
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
    "JWT_AUTH_SECURE": DEBUG,  # False for development
    "USER_DETAILS_SERIALIZER": "user.serializers.UserSerializer",
    "REGISTER_SERIALIZER": "core.serializers.CustomRegisterSerializer",
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
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVE_URLCONF": "core.urls",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
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

# ==== Database settings ====

if PROD:
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ==== Authentication settings ====

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


# === Allauth settings ===

ACCOUNT_EMAIL_VERIFICATION = "optional"


ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_SIGNUP_FIELDS = ["username*", "email*", "password1*", "password2*"]

ACCOUNT_LOGIN_METHODS = {"email"}


# ==== Email settings ====

if not PROD:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = BASE_DIR / "sent_emails"  # Directory to store sent emails


# ==== Google Drive settings ====
GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON = os.environ.get("GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON")
PROFILE_PIC_FOLDER_ID = os.environ.get("GOOGLE_DRIVE_PROFILE_PIC_FOLDER_ID")
BLOG_THUMBNAIL_FOLDER_ID = os.environ.get("GOOGLE_DRIVE_BLOG_THUMBNAIL_FOLDER_ID")


# ==== Middlewares ====


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


# === Static files (CSS, JavaScript, Images) ====
STATIC_URL = "/static/"

if PROD:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

WSGI_APPLICATION = "core.wsgi.application"

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
