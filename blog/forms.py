from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Post



class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body'
            ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2'
            ]

