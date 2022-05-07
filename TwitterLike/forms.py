from django import forms
from .models import Tweet


class CreatePost(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('desc', 'img')
