from pathlib import Path
import os, sys

# Localização do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Segurança do projeto
SECRET_KEY = 'django-insecure-^kuxm1h(@i^m_$)78nk(v889bdn83i(*_7@o=1b^bz&0@k32x$'

# Developers
DEBUG = True
ALLOWED_HOSTS = []

# Importando os diretórios.
sys.path.append(
    os.path.join(BASE_DIR, "Applications")
)


# Aplicativos internos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Aplicativos Externos
INSTALLED_APPS += [
    'django_extensions',
    'Users',
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

ROOT_URLCONF = 'Configurations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
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

WSGI_APPLICATION = 'Configurations.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#Configurações para login declaração de user 
AUTH_USER_MODEL = "Users.User" # Declarando nas configurações qual é o novo padrão de User
#LOGIN_REDIRECT_URL = 'ViewIndex' # Redirecionando para a pagina inicial depois de logar
#LOGIN_URL = 'ViewLogin' # Definindo a view padrão do Django de login


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

# Configurações básicas referentes a linguagem e horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Configurando arquivos estáticos
STATIC_URL = '/static/'




# Configurações de envio do e-mail

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "gomesmillateste@gmail.com"
# EMAIL_HOST_PASSWORD = "GomesMillateste1"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "michel.lemes@unincor.edu.br"
EMAIL_HOST_PASSWORD = "87028399dd"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
