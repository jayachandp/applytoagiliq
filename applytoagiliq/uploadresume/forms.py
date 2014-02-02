from django import forms
from uploadresume.models import Resume
from django.core.exceptions import ValidationError

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume