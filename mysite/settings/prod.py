from mysite.setting.base import *

with open('/tmp/settings_log','w+') as settings_log:
    settings_log.write("Using the prod settings")
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'supersecret',
        'PORT': '5432'
    }
}

DATABASES['default']['HOST'] = '/cloudsql/autointern-prod:us-east1:autointern-prod'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'

STATIC_URL = 'https://storage.googleapis.com/autointern-prod/static/'
