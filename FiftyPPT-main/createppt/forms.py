from django import forms
from .models import PPT

class PPTForm(forms.ModelForm):
    class Meta:
        model = PPT
        fields = ['title', 'image']
