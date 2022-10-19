from django import forms


class Register(forms.Form):
    email_id = forms.EmailField(max_length=100)
    passwd = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())

class Login(forms.Form):
    email_id=forms.EmailField(max_length=100)
    passwd=forms.CharField(widget=forms.PasswordInput())