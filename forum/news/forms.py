from .models import NewsArticle
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'pub_date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название доски'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарии. Макс. длина 10000'
            }),


        }



