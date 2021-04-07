from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,tag_interest




# Определяем новый класс настроек для модели User
class CustomUserAdmin(UserAdmin):
    form = UserAdmin.form
admin.site.register(User, CustomUserAdmin)
admin.site.register(tag_interest)