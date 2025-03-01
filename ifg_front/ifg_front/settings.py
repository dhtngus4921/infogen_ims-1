"""
Django settings for ifg_front project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import logging.config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1mqm8!s049l%ovo32nz$2yu%4e7i%w1puw@og+x08y)04*$o7='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'index',
    'main',
    'emp_api',
    'prj_api',
    'skil_api',
    'cmm_api',
    'cnc_api',
    'dili_api',
    'eval_api',
    'kpi_api',
    'stat_api',
    'site_api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'ifg_front.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
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

WSGI_APPLICATION = 'ifg_front.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ifg_ims',
        'USER': 'infogen',
        'PASSWORD': 'infogen',
        'HOST': '218.151.225.142',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/main/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MDDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
		},
	},
	'loggers': {
		'main': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
        'emp_api': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
        'skil_api': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
        'dili_api': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
        'prj_api': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
        'kpi_api': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
        'cmm_api': {  # django app
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': False,  # required to avoid double logging with root logger
		},
	},
}

SESSION_COOKIE_AGE = 60 * 10
SESSION_SAVE_EVERY_REQUEST = True

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)