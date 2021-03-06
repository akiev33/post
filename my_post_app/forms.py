from django import forms
from django.core.exceptions import ValidationError

from my_post_app.models import Post, Image


class PostForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Введите название поста'}))

    description = forms.CharField(max_length=225, label='Описание поста',
                                  widget=forms.TextInput(attrs={'placeholder': 'Введите описание поста'}))

    def clean(self):
        name = self.cleaned_data['name']
        if not len(name) > 6 and len(name) < 8:
            raise ValidationError('не правильно введено название')
        return self.cleaned_data


class MyPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'name', 'description', 'hashtag'
        )
        # exclude = ('name',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'image', 'post')