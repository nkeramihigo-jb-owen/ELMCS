from django.urls import path

from .views import (
    login_view,
    dashboard,
    logout_view,
    expatriate_profile,
    expatriate_documents,
    agency_expatriates,
    my_agency,
    agency_documents,
    government_agencies,
    government_expatriates,
    government_documents,
    government_work_permits,
    expatriate_detail,
    edit_expatriate,
    upload_expatriate_document,
    delete_expatriate_document,
    government_agency_detail,
)

urlpatterns = [
    path('login/', login_view, name='login'),


    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'expatriate/profile/',
        expatriate_profile,
        name='expatriate_profile'
    ),

    path(
        'expatriate/documents/',
        expatriate_documents,
        name='expatriate_documents'
    ),
    path(
    'agency/expatriates/',
    agency_expatriates,
    name='agency_expatriates'
),

   path(
    'agency/',
    my_agency,
    name='my_agency'
),

    path(
        'agency/documents/',
        agency_documents,
        name='agency_documents'
    ),

    path(
    'government/agencies/',
    government_agencies,
    name='government_agencies'
),
    path(
        'government/expatriates/',
        government_expatriates,
        name='government_expatriates'
    ),

    path(
    'government/documents/',
    government_documents,
    name='government_documents'
),

    path(
        'government/work-permits/',
        government_work_permits,
        name='government_work_permits'
    ),

    path(
    'expatriate/<int:expatriate_id>/',
    expatriate_detail,
    name='expatriate_detail'
),
    path(
    'government/expatriate/<int:expatriate_id>/edit/',
    edit_expatriate,
    name='edit_expatriate'
),

   path(
    'government/expatriate/<int:expatriate_id>/documents/upload/',
    upload_expatriate_document,
    name='upload_expatriate_document'
),
    path(
    'government/document/<int:document_id>/delete/',
    delete_expatriate_document,
    name='delete_expatriate_document'
),
    path(
    'government/agency/<int:agency_id>/',
    government_agency_detail,
    name='government_agency_detail'
),
]
