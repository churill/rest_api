from .base import *


#####################
# Security settings #
#####################

DEBUG = env.get_value('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = []


############
# Database #
############

DATABASES = {
    'default': env.db()
}
DATABASES['default'].update({
    'OPTIONS': {
        'driver': env('DATABASE_OPTIONS1'),
        'extra_params': env('DATABASE_OPTIONS2')
    }
})


###########
# Logging #
###########

LOGGING = {
    # バージョンは「1」固定
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # 開発用
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                      '%(message)s'
        },
        # ハンドラ
        'handlers': {
            # コンソール出力用ハンドラ
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'develop',
            },
        },
        # ロガー
        'logger': {
            # 自作アプリケーション全般のログを拾うロガー
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            # Django 本体が出すログ全般を拾うロガー
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            # 発行される SQL 文を出力するための設定
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }
}


##################
# Extra settings #
##################