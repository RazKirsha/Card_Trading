from django import forms
from .models import *


class WriteTopic(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['title', 'content']


class WriteComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'content']
