ALLOWED_HOSTS = ['sebanzian.pythonanywhere.com', 'localhost']

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Sebanzian$Django-blog',
        'USER': 'Sebanzian',
        'PASSWORD': 'f41f8c7123a5',
        'HOST': 'Sebanzian.mysql.pythonanywhere-services.com',
    }
}