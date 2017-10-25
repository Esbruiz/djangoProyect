from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='xtv#f@x^eiq7d33bqvep_14_f3qkq$%*8$c+bp5$fd=-y)tf_4')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
