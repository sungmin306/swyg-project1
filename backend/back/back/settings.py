"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import datetime
import json, os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")
#### SECRET_KEY 분리

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['.pythonantwhere.com']
ALLOWED_HOSTS = []
# Application definition

AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS = [
    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_filters',
    'django.contrib.sites',
    'allauth',
    #'allauth.account',
    #'rest_auth.registration',
    #DRF Authentication
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_auth',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework_simplejwt',
    'allauth.socialaccount',
    #react 연동
    'corsheaders',

    #myapp
    #'account', #로그인로그아웃
    'delivery', #공동배달
    'notice_board', #게시판
    'accounts'
]
SITE_ID = 1
#AUTH_USER_MODEL = 'accounts.User'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# rest-auth 로그인할때 username 빼고 email로만 회원가입 하게 하는 setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


ACCOUNT_AUTHENTICATION_METHOD = 'email' # 로그인 인증 방법 email 로 설정 ACCOUNT_EMAIL_REQUIRED = True 와 같이 사용
ACCOUNT_EMAIL_REQUIRED = True    # 로그인 인증 방법 email 로 설정
ACCOUNT_USERNAME_REQUIRED = False# 로그인 할때 username 이 필요없더라도 회원가입 시 username을 필수로 적게끔 함
CCOUNT_EMAIL_VERIFICATION = 'none' # 회원가입 과정에서 이메일 인증 사용 X
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

AUTHENTICATION_BACKENDS = (
 "django.contrib.auth.backends.ModelBackend",
 "allauth.account.auth_backends.AuthenticationBackend",
)
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #Authentication을 모든 view에서 동일하게 사용하는 setting
        #'rest_framework.authentication.BasicAuthentication',  #username & password 로 식별하는 가장 기본적인 방식
        #'rest_framework.authentication.SessionAuthentication', #django default session backend 이용하는 방식 -> 무슨 소리인지 모르겠다
        #'rest_framework.authentication.TokenAuthentication', # Postman에서 돌릴때 client - server api 방식
        'rest_framework_simplejwt.authentication.JWTAuthentication', # simple jwt 방식 사용
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
#### email login-------------------------------------

REST_USE_JWT = True

SIMPLE_JWT = {
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'ACCESS_TOKEN_LIFETIME' : datetime.timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME' : datetime.timedelta(days=7)

}

# JWT_AUTH = {
#     'JWT_SECRET_KEY': SECRET_KEY,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
# }

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     # react 연동
    'django.middleware.common.CommonMiddleware', # react 연동
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ORIGIN_WHITELIST = [
    'https://localhost:3000',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
