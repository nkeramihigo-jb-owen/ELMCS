from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AgencyUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = User.Role.AGENCY
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user