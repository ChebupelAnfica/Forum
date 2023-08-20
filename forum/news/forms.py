from django import forms
from .models import NewsArticle

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content']