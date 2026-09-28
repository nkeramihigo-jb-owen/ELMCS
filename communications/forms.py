from django import forms

from .models import Request, Complaint

class RequestForm(forms.ModelForm):


    class Meta:
        model = Request

        fields = (
            'subject',
            'description',
        )

        widgets = {
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Enter request subject',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe your request...',
                    'rows': 6,
                }
            ),
        }

class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = (
            'subject',
            'description',
        )

        widgets = {
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Enter complaint subject',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe your complaint...',
                    'rows': 6,
                }
            ),
        }

class ComplaintResponseForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = (
            'status',
            'response',
        )

        widgets = {
            'status': forms.Select(),

            'response': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your response to the expatriate...',
                    'rows': 6,
                }
            ),
        }

class RequestResponseForm(forms.ModelForm):

    class Meta:
        model = Request

        fields = (
            'status',
            'response',
        )

        widgets = {
            'status': forms.Select(),

            'response': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your response to the expatriate...',
                    'rows': 6,
                }
            ),
        }