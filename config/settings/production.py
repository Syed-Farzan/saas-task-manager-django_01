import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", SECRET_KEY)
