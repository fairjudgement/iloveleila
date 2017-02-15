from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="My Love ;)    ", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Shorter version of mine ;)    ", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('baslik', 'yazi',)