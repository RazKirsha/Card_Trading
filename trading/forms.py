from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class MakeBidModelForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['offered_price']
