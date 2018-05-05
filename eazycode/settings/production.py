from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ("gunicorn",)

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default' : dj_database_url.config(
        default = 'sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}

MIDDLEWARE_CLASSES += (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
