"""
Django settings for root project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kx#49@$(2auqu9=v9w359m-h0vyv+6k^dr_w&dn-c7pk0&9^qu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # For Session ID
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
# Add here the newly created apps using "python manage.py startapp postgis" command
# No need that the app should be outside the root folder, it could be inside (accd to some
# reading) but in that case one need to change the urls also accordingly
    'postgis',
# For CORS, but before that install it "pip install django-cors-headers", 
# url "https://github.com/ottoyiu/django-cors-headers/". 
# All the CORS related changes are here in settings.py only
    'corsheaders',
    'raster',
)

MIDDLEWARE_CLASSES = (
    # For Session ID
    'django.contrib.sessions.middleware.SessionMiddleware',
    # For CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # For CSRF
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'userdetails.middleware.crossdomainxhr.XsSharing',
)
# For CORS
CORS_ORIGIN_ALLOW_ALL = True
# For CORS
CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS'
    )


ROOT_URLCONF = 'root.urls'

WSGI_APPLICATION = 'root.wsgi.application'

TEMPLATE_CONTEXT_PROCESSOR = (
	# For CSRF. We need this to allow csrf from templates
	'django.core.context_processors.csrf',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Following are the Db connections, one can connect to any Db and number of it.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
# It's the Db name
        'NAME': 'default',
# Db superuser
	'USER': 'postgres',
	'PASSWORD': 'zia123',
# Normally HOST should be blank for localhost (like 'HOST': '') but there was some problem, so 127.0.0.1
	'HOST': '127.0.0.1',
# PORT should also be blank if postgresql is running on 5432 port
	'PORT': '5432',
    },
    'postgisdb': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgisdb',
	'USER': 'postgres',
	'PASSWORD': 'zia123',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    },
    'trafficdb': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trafficdb',
	'USER': 'postgres',
	'PASSWORD': 'zia123',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    },
    'zia': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zia',
	'USER': 'postgres',
	'PASSWORD': 'zia123',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    },
    # Making an actual Db in the Db and a corresponding connection here is a MANUAL job
    # Otherwise soo many Db connections is possible
    'mohammed.zia33@gmail.com': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mohammed.zia33@gmail.com',
	'USER': 'postgres',
	'PASSWORD': 'zia123',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    },
    'ashokyadav006@gmail.com': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ashokyadav006@gmail.com',
	'USER': 'postgres',
	'PASSWORD': 'zia123',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    },
    'campus_itu_maslak': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'campus_itu_maslak',
	'USER': 'postgres',
	'PASSWORD': 'zia123',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

RASTER_USE_CELERY = True
