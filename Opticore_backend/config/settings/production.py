from .base import *

DEBUG = False

# En producción define esto desde .env
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Seguridad básica (puedes endurecer después)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True