from django.contrib import admin
from .models import Expatriate, Document

@admin.register(Expatriate)
class ExpatriateAdmin(admin.ModelAdmin):
    list_display = (
    'user',
    'nationality',
    'passport_number',
    'job_title',
    'employer',
    'work_permit_expiry',
    'agency',
    )


    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'passport_number',
        'nationality',
        'employer',
    )

    list_filter = (
        'nationality',
        'gender',
        'agency',
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
    'title',
    'document_type',
    'expatriate',
    'expiry_date',
    'uploaded_at',
    )


    search_fields = (
        'title',
        'expatriate__user__username',
        'expatriate__user__first_name',
        'expatriate__user__last_name',
    )

    list_filter = (
        'document_type',
        'expiry_date',
    )

