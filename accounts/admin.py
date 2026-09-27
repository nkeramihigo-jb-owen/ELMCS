from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    ('ELMCS Information', {
    'fields': ('role',),
    }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('ELMCS Information', {
            'fields': ('role',),
        }),
    )

