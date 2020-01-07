from django import forms
from shopapp.models import Student
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'