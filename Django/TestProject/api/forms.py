from django import forms
from .models import User
'''
class Registration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
'''

class Registration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email']