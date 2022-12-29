from django.db import models
from django.contrib import admin

class Employee(models.Model):
    unique_number=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    job=models.CharField(max_length=100)
    email=models.EmailField()
    

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('unique_number','name','age','job','email')