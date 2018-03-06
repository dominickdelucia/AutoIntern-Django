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

DATABASES['default']['host'] = '/cloudsql/autointern-uat:us-east1:autointern-prod'
STATIC_URL = 'https://storage.googleapis.com/autointern-prod/static/'