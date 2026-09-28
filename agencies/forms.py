from django import forms
from .models import Agency


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = (
            'name',
            'registration_number',
            'address',
            'phone',
            'email',
        )