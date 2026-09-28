from django.urls import path

from .views import (
    create_request,
    my_requests,
    create_complaint,
    my_complaints,
    officer_requests,
    officer_complaints,
    handle_complaint,
    handle_request,
    my_notifications,
)

urlpatterns = [


path(
    'requests/',
    my_requests,
    name='my_requests'
),

path(
    'requests/create/',
    create_request,
    name='create_request'
),

path(
    'complaints/',
    my_complaints,
    name='my_complaints'
),

path(
    'complaints/create/',
    create_complaint,
    name='create_complaint'
),

path(
    'officer/requests/',
    officer_requests,
    name='officer_requests'
),

path(
    'officer/complaints/',
    officer_complaints,
    name='officer_complaints'
),

path(
    'officer/complaints/<int:complaint_id>/',
    handle_complaint,
    name='handle_complaint'
),

path(
    'officer/requests/<int:request_id>/',
    handle_request,
    name='handle_request'
),

path(
    'notifications/',
    my_notifications,
    name='my_notifications'
),
]
