"""
Django settings for tree project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aoujt5zb)!i1rrhqnhvpa^h@9tit$&9zlerp1+at+@*d%8x09j'

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
    'app',
    'geoposition',
    'plot',
    'hw1',
    'lua',
    'questions',
    # 'contacts',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tree.urls'
# ROOT_URLCONF = 'plot.urls'

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
                'django.core.context_processors.request',#  <a href="{{request.META.HTTP_REFERER}}">Go back</a>
            ],
        },
    },
]

WSGI_APPLICATION = 'tree.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#######################################################
# # From the Django for scientists tutorial

def relative2absolute_path(relative_path):
    """Return the absolute path correspodning to relative_path."""
    dir_of_this_file = os.path.dirname(os.path.abspath(__file__))
    return dir_of_this_file + '/' + relative_path

# TEMPLATE_DIRS = [relative2absolute_path('../../tree/hw1/static'),
# ]





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # # From the Django for scientists tutorial
        'NAME': relative2absolute_path('../database.db')
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# from django.utils.translation import ugettext_lazy as _
# LANGUAGES = (
#     ('en', _('English')),
#     ('ca', _('Catalan')),
#     ('pt-br', _('Portuguese')),
#     ('nl', _('Dutch')),
# )

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

######################################################################
# Added at the start
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = ''

# Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(os.path.dirname(__file__), 'static'),
# )
#####################################################################
# # Added for the graph
# SETTINGS_DIR = os.path.dirname(__file__)
# PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
# PROJECT_PATH = os.path.abspath(PROJECT_PATH)
# STATIC_PATH = os.path.join(PROJECT_PATH,'static')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     STATIC_PATH,
# )


#########################################################
#
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}





