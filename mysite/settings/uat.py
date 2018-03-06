from mysite.setting.base import *

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
DATABASES['default']['host'] = '/cloudsql/autointern-uat:us-east1:autointern-uat'
STATIC_URL = 'https://storage.googleapis.com/autointern-uat/static/'