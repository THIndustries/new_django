"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-txbg_iy%01fqi(piyo-g0_9c9+*=9puryf1x=rp*fmit9@$u&3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.1.130',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'gamesapp',
    'myapp2',
    'homeworkapp',
    'myapp3',
    'myapp4',
    'myapp5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = '/temp'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

#Обрати внимание: Два нижних параметра для работы с img добавил сам, изначально их не было:
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, # Отключить существующие логи? False (нет)
    'formatters': { # ключ formatters и внутри два формата
        'simple': { # обычное форматирование
            'format': '%(levelname)s %(message)s' # уровень и сообщение
        },
        'verbose': { # более глубокое форматирование
            'format': '{levelname} {asctime} {module} {process} {thread} {message}',
            'style': '{', # указываем стиль для более удобного чтения сообщения
        },
    },
    'handlers': { #обработчик handlers
      'console': { # консольный обработчик
            'class': 'logging.StreamHandler', # Выводим в консоль информацию, используя StreamHandler
            'formatter': 'verbose', # добавляем параметр formsatter
        },
      'file': { # файловый обработчик
            'class': 'logging.FileHandler', # Записываем в файл информацию, используя FileHandler
            'filename': './log/django.log', # Прописываем путь до нужного каталога, где хранится лог
            'formatter': 'verbose', # и иту добавляем тип форматирования
        },
    },
    'loggers': { # Логгер. Логгеров тут у нас два: django и myapp
        'django': { # Здесь логгируем все данные этого приложения, сервера.
            'handlers': ['console', 'file'], # В качестве обработчика указываем оба варианта
            'level': 'INFO', # Уровень логирования
        },
        'myapp': { # Здесь логгируем события наего приложения.
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True, # Если есть высокостоящие логгеры, то использовать их? True
        },
        'gamesapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp4': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}