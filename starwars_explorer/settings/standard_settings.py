from starwars_explorer.settings.base_settings import *

INSTALLED_APPS += [
    # Apps
    'starwars.apps.StarwarsConfig',
    # Third party
    'django_cleanup',
]

MIDDLEWARE += [
    # Django-htmlmin
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]


# DJANGO LOCAL-MEMORY CACHE ----------------------------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'Starwars',
    }
}


# STATIC FILES -----------------------------------------------------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'public'

MEDIA_URL = 'assets/'
MEDIA_ROOT = BASE_DIR / 'datasets'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)


# DJANGO-HTMLMIN ----------------------------------------------------------------------------------

HTML_MINIFY = False
EXCLUDE_FROM_MINIFYING = ('portfolioadmin/')
KEEP_COMMENTS_ON_MINIFYING = False
CONSERVATIVE_WHITESPACE_ON_MINIFYING = True
