from mysite.settings.base import *

with open('/tmp/settings_log','w+') as settings_log:
    settings_log.write("Using the uat settings")
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'winnerwinner',
        'PORT': '5432'
    }
}

DATABASES['default']['HOST'] = '/cloudsql/autointern-uat:us-east1:autointern-uat'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'

STATIC_URL = 'https://storage.googleapis.com/autointern-uat/static/'
