import os
import environ
from pathlib import Path
from django.core.mail import send_mail

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-xu*kflhns6ou3_e!x+cbjdhg@rgk#f^eimv#)zu&)kpl2-p1#@'

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
 
DATABASES = {
    'default': env.db()
}

# Application definition
# 自作アプリを追加する場合、上書きの必要なければ、下へ追加する
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'accounts.apps.AccountsConfig',
    'django_bootstrap5',
    'party.apps.PartyConfig',
    "bootstrap_datepicker_plus",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static_local" ] # 開発環境

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media_local" # 開発環境

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SecurityMiddleware：HTTPアクセスをHTTPSのURLへリダイレクトする
# SECURE_SSL_REDIRECT = True

AUTH_USER_MODEL = 'accounts.CustomUser'

# django-allauth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', #デフォルト
    'allauth.account.auth_backends.AuthenticationBackend', #追加
)

#認証方式を 「メールアドレスとパスワード」 に変更
ACCOUNT_AUTHENTICATION_METHOD = 'email'  #認証方式をメールアドレスにする
ACCOUNT_USERNAME_REQUIRED = True  #登録時にユーザー名を必要とする
ACCOUNT_EMAIL_REQUIRED = True  #メールアドレスを必須項目にする
ACCOUNT_EMAIL_VERIFICATION = 'none'  #登録確認メールを送信しない
ACCOUNT_LOGOUT_ON_GET = True #確認画面無しのログアウト

SITE_ID = 1
LOGIN_REDIRECT_URL = 'party:index'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# django-bootstrap-datepicker-plus の日時表記カスタマイズ
BOOTSTRAP_DATEPICKER_PLUS = {
    "options": {
        "locale": "ja",
    },
    "variant_options": {
        "time": {
            "format": "HH:mm",
        },
    }
}

#allauth formのカスタム
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm',
    'login': 'accounts.forms.CustomLoginForm',
    'reset_password': 'accounts.forms.CustomResetPasswordForm',
    'reset_password_from_key': 'accounts.forms.CustomResetPasswordKeyForm',
    'change_password': 'accounts.forms.CustomChangePasswordForm',
    'add_email': 'accounts.forms.CustomAddEmailForm',
    'set_password': 'accounts.forms.CustomSetPasswordForm',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #開発環境

# Gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

subject = "This is MailSubject"
message = "This is\nMailContent"
from_email = 'drinkingpartyms@gmail.com'
recipient_list = ["comukichi@gmail.com"]
send_mail(subject, message, from_email, recipient_list)
