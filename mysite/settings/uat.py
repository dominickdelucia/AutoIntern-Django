from mysite.setting.base import *

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