from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','profile_pic']


class LoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput)