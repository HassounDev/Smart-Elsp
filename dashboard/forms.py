from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Adress'}))
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
