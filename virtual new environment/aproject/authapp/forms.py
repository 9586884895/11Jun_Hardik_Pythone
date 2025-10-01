from django import forms
from.models import *

class signup(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'