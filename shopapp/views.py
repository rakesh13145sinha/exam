from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shopapp.models import Student
from .import forms
import datetime
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    count=User.objects.count()
    d=datetime.datetime.now()
    return render(request,'templates/shopapp/home.html',{'date':d,'count':count})
@login_required
def java(request):
    return render(request,'templates/shopapp/java.html',)
@login_required
def python(request):
    return render(request, 'templates/shopapp/python.html')
@login_required
def sql(request):
    return render(request, 'templates/shopapp/sql.html')

#for student form

def student_form(request):
    form=forms.Student_form
    if request.method=='POST':
        form=forms.Student_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'templates/shopapp/home.html')
    
    return render(request,'templates/shopapp/student_form.html',{'form':form})
#logout form
def logout(request):
    return render(request,'templates/shopapp/logout.html')
#password change
#def password_change(request):
#    return render(request,'registration/password_change_form')
#password change done!
#def password_done(request):
#    return render(request,'registration/password_change_done.html')
#for signup
def signup(request):
    sign = forms.SignUpForm
    if request.method=='POST':
        sign = forms.SignUpForm(request.POST)
        if sign.is_valid():
            sign.save()
        return render(request,'templates/shopapp/home.html')
    return render(request,'templates/shopapp/signup.html',{'sign':sign})
#for student list display
def display(request):
    display_list=Student.objects.all()
    return render(request,'templates/shopapp/list.html',{'display_list':display_list})
#it is class base view to use signup
def class_signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'templates/shopapp/home.html')
    return render(request,'templates/shopapp/sign_c.html',{'form':form})