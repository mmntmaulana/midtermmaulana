from django.forms import ModelForm
from .models import Post


class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']
