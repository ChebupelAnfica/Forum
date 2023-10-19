from .models import SoftArticle
from django.forms import ModelForm, TextInput, Textarea


class SoftForm(ModelForm):
    class Meta:
        model = SoftArticle
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




