from django.contrib import admin

from steward.models import UserLoginHistory
from django.contrib.auth.models import Permission

admin.site.site_header = '大管家进销存'
admin.site.site_title = '大管家进销存'


class UserLoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('history_id', 'uid', 'token', 'ip', 'create_time', 'remember')
    list_filter = ('uid',)


class AuthPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename', 'id')
    list_filter = ('name', 'codename')


# 注册实体类到admin模块
admin.site.register(UserLoginHistory, UserLoginHistoryAdmin)
admin.site.register(Permission, AuthPermissionAdmin)
