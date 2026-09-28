from django.urls import path

from .views import (
    government_verification,
    government_verifications,
)


urlpatterns = [

    path(
        'government/verify/<int:expatriate_id>/',
        government_verification,
        name='government_verification'
    ),

    path(
    'government/verifications/',
    government_verifications,
    name='government_verifications'
),

]