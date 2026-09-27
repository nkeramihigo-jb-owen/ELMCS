from django.contrib import admin
from .models import Verification

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = (
    'expatriate',
    'status',
    'verified_by',
    'verified_at',
    'created_at',
    )


    search_fields = (
        'expatriate__user__username',
        'expatriate__user__first_name',
        'expatriate__user__last_name',
        'expatriate__passport_number',
    )

    list_filter = (
        'status',
        'created_at',
    )

