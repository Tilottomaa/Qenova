from django import forms

from .models import User,OrganizationUser

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','profile_pic']


class LoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput)


class OrganizationForm(forms.ModelForm):

    class Meta:

        model = OrganizationUser

        fields = [
            'organization_name',
            'email',
            'password',
            'logo',
            'working_hours'
        ]





class OrganizationLoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )