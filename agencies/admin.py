from django.contrib import admin
from .models import Agency

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'registration_number',
    'phone',
    'email',
    'created_at',
    )
    search_fields = (
    'name',
    'registration_number',
    'email',
    )
