from django import forms

from .models import Readlist

class ReadlistCreateForm(forms.ModelForm):
    class Meta:
        model = Readlist
        fields = ['name', 'manga']