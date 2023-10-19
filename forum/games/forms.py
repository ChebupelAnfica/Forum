from .models import GamesArticle
from django.forms import ModelForm, TextInput, Textarea


class GameForm(ModelForm):
    class Meta:
        model = GamesArticle
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





