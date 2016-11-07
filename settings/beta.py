from .base import *
"""
DATABASES = {
	'default':{
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'Uzzije$default',
		'USER': 'Uzzije',
		'PASSWORD': 'DaKuimcv1',
		'HOST': 'Uzzije.mysql.pythonanywhere-services.com',
	}
}
"""
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': os.environ['RDS_DB_NAME'],
		'USER': os.environ['RDS_USERNAME'],
		'PASSWORD': os.environ['RDS_PASSWORD'],
		'HOST': os.environ['RDS_HOSTNAME'],
		'PORT': os.environ['RDS_PORT'],
	}
}