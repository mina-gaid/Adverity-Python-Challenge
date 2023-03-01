from starwars_explorer.settings.standard_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'starwars-explorer.com']

MIDDLEWARE += [
    # Django-WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# DATABASE ---------------------------------------------------------------------------------------

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Cloud Database for Production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'ec2-54-228-125-183.eu-west-1.compute.amazonaws.com',
        'PORT': '',
        'OPTIONS': {"sslmode": "require"},
    }
}


# DJANGO-STORAGE ----------------------------------------------------------------------------------

# Uploading blob to Cloud storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_AUTO_CREATE_BUCKET = True
AWS_S3_REGION_NAME = 'eu-gb'
AWS_STORAGE_BUCKET_NAME = 'starwars-explorer'
AWS_S3_ENDPOINT_URL = 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud'


# DJANGO-ALLAUTH ----------------------------------------------------------------------------------

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
