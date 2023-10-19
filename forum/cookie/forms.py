from .models import CookieArticle
from django.forms import ModelForm, TextInput, Textarea


class CookieForm(ModelForm):
    class Meta:
        model = CookieArticle
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


