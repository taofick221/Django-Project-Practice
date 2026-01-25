from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student,Profile

class StudentForms(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Name','Age','Email']
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','image']
    
    
    