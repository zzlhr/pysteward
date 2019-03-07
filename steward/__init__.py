import pymysql
from django.apps import AppConfig

pymysql.install_as_MySQLdb()


class StewardConfig(AppConfig):
    name = 'steward'
    verbose_name = '进销存'
    verbose_name_plural = verbose_name


default_app_config = 'steward.StewardConfig'
