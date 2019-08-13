from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ('program', 'title')
        widgets = {
                "program": forms.Textarea(),
            }

