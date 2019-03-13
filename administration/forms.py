from django.contrib.auth import get_user_model
from django import forms


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label_suffix='')
    email = forms.EmailField(label='Email', label_suffix='')

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']