"""
Django settings for SharedSpaceWMS project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--8m24a%a5r_hy@a$woz^f1(&k983$pl^4lijdaur4*3m3i857v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # APPS
    'admin_app',
    'customer_app',
    'order_app',
    'product_app',
    # Installed Modules
    'drf_yasg',
    'drf_generators',
    'rest_framework'
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

ROOT_URLCONF = 'SharedSpaceWMS.urls'

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

WSGI_APPLICATION = 'SharedSpaceWMS.wsgi.application'


DATABASE_ROUTERS = ['SharedSpaceWMS.DatabaseRouterApp.DatabaseRouterApp']
DATABASE_APPS_MAPPING = {'admin_app':'default', 'customer_app':'customer', 'order_app':'order', 'product_app':'product'}



## PROD DATABASE DETAILS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'admins',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT':'5432',
        
        # 'PORT' : os.environ.get("AUTH_SQL_PORT"),
        'options':{
            'init_command': 'SET innodb_strict_mode=1',
            # "threaded":True,
            'skip-ssl':True,
            'pooling': {
                "max_size": 10,
                "max_idle_time": 1
            }
        },
        'CONN_MAX_AGE': 0
    },

    'customer': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'customer',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT':'5432',
        # 'PORT' : os.environ.get("MARKETING_SQL_PORT"),
        'options':{
            'init_command': 'SET innodb_strict_mode=1',
            # "threaded":True,
            'skip-ssl':True,
            'pooling': {
                "max_size": 10,
                "max_idle_time": 1
            }
        },
        'CONN_MAX_AGE': 0
    },

    'order': {
       'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'order',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT':'5432',
        'options':{
            'init_command': 'SET innodb_strict_mode=1',
            # "threaded":True,
            'skip-ssl':True,
            'pooling': {
                "max_size": 10,
                "max_idle_time": 1
            }
        },
        'CONN_MAX_AGE': 0
    },

    'product': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'product',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT':'5432',
        'options':{
            'init_command': 'SET innodb_strict_mode=1',
            # "threaded":True,
            'skip-ssl':True,
            'pooling': {
                "max_size": 10,
                "max_idle_time": 1
            }
        },
        'CONN_MAX_AGE': 0
    },
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

AUTH_USER_MODEL = 'admin_app.Admins'

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

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
