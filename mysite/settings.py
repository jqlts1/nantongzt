#coding:utf8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '89)zusb%aj)huohwin_c4snx%z(d(kh--j_7mvria0!u#(_sab'
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'DjangoUeditor',
)






MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)



ROOT_URLCONF = 'mysite.urls'




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'web/templates/jinja2'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'mysite.jinja2.environment',  #myroject就是项目的地址,不是跟目录
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {

            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nantongzt',    #数据库名
        'USER': 'jqlts1',    #用户名
        'PASSWORD': 'zhangte7941',    #密码
        'HOST': '118.184.31.136',  #链接id ,空为本地,可以设置绝对路径
        'PORT': '3306', #端口号
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'nantongzt',    #数据库名
#         'USER': 'root',    #用户名
#         'PASSWORD': 'zhangte',    #密码
#         'HOST': '',  #链接id ,空为本地,可以设置绝对路径
#         'PORT': '3306', #端口号
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'woke',    #数据库名
#         'USER': 'jqlts1',    #用户名
#         'PASSWORD': 'zhangte7941',    #密码
#         'HOST': '118.184.31.136',  #链接id ,空为本地,可以设置绝对路径
#         'PORT': '3306', #端口号
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'web/static')


# 公共的 static 文件，比如 jquery.js 可以放这里，这里面的文件夹不能包含 STATIC_ROOT
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
)


# upload folder
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# log配置
LOG_FILE = "./all.log"

LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,

        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
                }
            },
        'formatters': {
            'simple': {
                'format': '[%(levelname)s] %(module)s : %(message)s'
                },
            'verbose': {
                'format':
                    '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
                }
            },

        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
                },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
                },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'verbose',
                'filename': LOG_FILE,
                'mode': 'a',
                },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['require_debug_false']
                }
            },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
                },
            'django': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
                },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': True,
                },
            }
        }


# cache配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
    'memcache': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': 'unix:/home/billvsme/memcached.sock',
        'LOCATION': '127.0.0.1:11211',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
}


# 分页配置
PAGE_NUM = 25

# email配置
# 如果想要支持ssl (比如qq邮箱) 见 https://github.com/bancek/django-smtp-ssl
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''                       # SMTP地址 例如: smtp.163.com
EMAIL_PORT = 25                       # SMTP端口 例如: 25
EMAIL_HOST_USER = ''                  # 我自己的邮箱 例如: xxxxxx@163.com
EMAIL_HOST_PASSWORD = ''              # 我的邮箱密码 例如  xxxxxxxxx
EMAIL_SUBJECT_PREFIX = u'vmaig'       # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True                  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 七牛配置
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''

# 网站标题等内容配置
WEBSITE_TITLE = u'南通私家侦探|南通私人侦探'
WEBSITE_WELCOME = u'南通大众商务调查有限公司'
author = u"南通侦探"

