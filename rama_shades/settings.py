from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # My Apps
    'store',
    'django_countries',
    'users',

    # Third Party
    'crispy_forms',

    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # For All Auth
    'django.contrib.sites',

    # all Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rama_shades.urls'

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
                'store.context_processors.cart_processor'

            ],
        },
    },
]

WSGI_APPLICATION = 'rama_shades.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DB_USERNAME"),
        'PASSWORD': os.getenv("DB_Password"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # existing backend
    'allauth.account.auth_backends.AuthenticationBackend',
)


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ((BASE_DIR / "static"),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# All Auth settings
SITE_ID = 3
LOGIN_REDIRECT_URL = '/'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_VERIFICATION = 'none'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STRIPE_PUBLIC_KEY = 'pk_test_1xQAlNLxJp2PKphMFaFP1pGG'
STRIPE_SECRET_KEY = 'sk_test_CKKNLKwPYCYsILKx3dDfrZ9q'

ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'users.forms.SignUpForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}
