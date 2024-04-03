from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Recipe


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжз'
                     'ийклмнопрстуфхцчшщьыъэюя0123456789- ')
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else ('Должны присутствовать '
                                                'только русские символы, '
                                                'дефис и пробел.')

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Категория не выбрана', label='Категория')

    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'content',
                  'photo', 'is_published', 'cat', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')

