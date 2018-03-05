from mysite.setting.base import *

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