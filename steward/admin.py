from django.contrib import admin

# from .models import UserLoginHistory
from . import models

admin.site.register(models.UserLoginHistory)
admin.site.register(models.User)
