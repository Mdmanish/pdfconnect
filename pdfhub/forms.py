from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class FileUploadForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
