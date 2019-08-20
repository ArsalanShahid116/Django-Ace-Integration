from django import forms
from .models import Code
from django.contrib.auth import get_user_model

class CodeForm(forms.ModelForm):
    author = forms.ModelChoiceField(
            widget=forms.HiddenInput,
            queryset=get_user_model().
            objects.all(),
            disabled=True,
            )

    class Meta:
        model = Code
        fields = ('author', 'title', 'description', 'body')
        widgets = {
                  "body": forms.Textarea(),
                }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('author')
        super(CodeForm, self).__init__(*args, **kwargs)
