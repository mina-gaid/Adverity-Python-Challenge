from starwars_explorer.settings.standard_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MIDDLEWARE += [
    # Django-WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# STATIC FILES -----------------------------------------------------------------------------------

# WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# DATABASE ---------------------------------------------------------------------------------------

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
