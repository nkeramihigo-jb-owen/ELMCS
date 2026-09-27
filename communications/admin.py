from django.contrib import admin
from .models import Request, Complaint, Notification

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
    'subject',
    'expatriate',
    'status',
    'responded_by',
    'created_at',
    'updated_at',
    )


    search_fields = (
        'subject',
        'expatriate__user__username',
        'expatriate__user__first_name',
        'expatriate__user__last_name',
    )

    list_filter = (
        'status',
        'created_at',
    )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
    'subject',
    'expatriate',
    'status',
    'responded_by',
    'created_at',
    'updated_at',
    )


    search_fields = (
        'subject',
        'expatriate__user__username',
        'expatriate__user__first_name',
        'expatriate__user__last_name',
    )

    list_filter = (
        'status',
        'created_at',
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
    'recipient',
    'title',
    'is_read',
    'created_at',
    )


    search_fields = (
        'recipient__username',
        'recipient__first_name',
        'recipient__last_name',
        'title',
        'message',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

