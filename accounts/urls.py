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
]
