from django import forms


class CreatePost(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)
    img = forms.ImageField(required=False)
