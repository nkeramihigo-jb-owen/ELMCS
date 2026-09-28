from django import forms
from .models import Expatriate, Document


class ExpatriateForm(forms.ModelForm):

    class Meta:
        model = Expatriate

        fields = (
            'agency',
            'date_of_birth',
            'nationality',
            'passport_number',
            'gender',
            'phone',
            'address_in_uganda',
            'job_title',
            'employer',
            'employment_start_date',
            'employment_end_date',
            'work_permit_number',
            'work_permit_expiry',
        )

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'employment_start_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'employment_end_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'work_permit_expiry': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def __init__(self, *args, **kwargs):
        hide_agency = kwargs.pop('hide_agency', False)

        super().__init__(*args, **kwargs)

        if hide_agency:
            self.fields.pop('agency')


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document

        fields = (
            'document_type',
            'title',
            'file',
            'expiry_date',
        )

        widgets = {
            'expiry_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

