from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = ["username", "email", "password"]
        fields = ["first_name" ,"last_name" , "username","email","password"]
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]