from django import forms
from .models import News

class ArticleForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


