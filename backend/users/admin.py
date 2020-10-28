# User models admin

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User


class CustomUserAdmin(UserAdmin):
    # User Model Admin

    list_display = ('legajo', 'username', 'first_name', 'last_name', 'is_staff')

    list_filter = ('is_staff', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
