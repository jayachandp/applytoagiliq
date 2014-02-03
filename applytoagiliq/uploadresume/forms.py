from django import forms
from uploadresume.models import Resume
from django.core.exceptions import ValidationError

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
    
    def clean(self, *args, **kwargs):
        super(ResumeForm, self).clean(*args, **kwargs)
        if self.cleaned_data.get('first_name') == '':
            raise ValidationError("First name can't be null")
        if self.cleaned_data.get('last_name') == '':
            raise ValidationError("Last name can't be null")
        if self.cleaned_data.get('project_url') == '':
            raise ValidationError("Project URL can't be null")
        if self.cleaned_data.get('code_url') == '':
            raise ValidationError("Code URL name can't be null")
        if not 'resume' in self.files:
            raise ValidationError("Please upload your resume")