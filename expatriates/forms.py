from django import forms

from accounts.models import User
from .models import Expatriate,Document


class ExpatriateForm(forms.ModelForm):

    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = Expatriate
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
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
        ]

    def __init__(self, *args, hide_agency=False, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_of_birth'].widget = forms.DateInput(
            attrs={'type': 'date'}
        )

        self.fields['employment_start_date'].widget = forms.DateInput(
            attrs={'type': 'date'}
        )

        self.fields['employment_end_date'].widget = forms.DateInput(
            attrs={'type': 'date'}
        )

        self.fields['work_permit_expiry'].widget = forms.DateInput(
            attrs={'type': 'date'}
        )

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'This username is already in use.'
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise forms.ValidationError(
                'Password must be at least 8 characters long.'
            )

        return password




class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = [
            'document_type',
            'title',
            'file',
            'expiry_date',
        ]

        widgets = {
            'expiry_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }    