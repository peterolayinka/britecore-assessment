from .base import *
# import raven

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.environ.get('SECRET_KEY', '1234567890qwertyuiop')

# ALLOWED_HOSTS = ['*']

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


AWS_STORAGE_BUCKET_NAME = 'britecore-assessment'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_IS_GZIPPED = True
GZIP_CONTENT_TYPES = (
   'text/css',
   'application/javascript',
   'application/x-javascript',
   'text/javascript',
   'application/vnd.ms-fontobject',
   'application/font-sfnt',
   'application/font-woff',
)

AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'staticfiles'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'