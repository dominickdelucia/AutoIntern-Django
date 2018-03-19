from mysite.settings.base import *


DEBUG = True

# Database
# [START dbconfig]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'winnerwinner',
        'PORT': '5432',
    },
}

DATABASES['default']['HOST'] = '/cloudsql/autointern-uat:us-east1:autointern-uat'

if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'
# [END dbconfig]

# Static files (CSS, JavaScript, Images)
# [START staticurl]
STATIC_URL = 'https://storage.googleapis.com/autointern-uat/static/'
STATIC_ROOT = 'static/'
# [END staticurl]
