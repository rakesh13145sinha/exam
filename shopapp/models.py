from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=52)
    father_name=models.CharField(max_length=52)
    roll=models.CharField(max_length=52)
    s_name=models.CharField(max_length=52)
    address=models.CharField(max_length=52)
    email=models.EmailField()
    password=models.CharField(max_length=30)
