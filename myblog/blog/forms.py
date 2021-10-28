from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    author = forms.CharField(label='Author', max_length=16)
    title = forms.CharField(label='Title', max_length=150)
    entry = forms.CharField(label='', widget=forms.Textarea)

    class Meta:
        model = Blog
        fields = ('author', 'title', 'entry', )
