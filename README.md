# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:

### STEP 2:

### STEP 3:

Write your own steps

## PROGRAM
### model.py
```python
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
```
### admin.py
```python
from django.contrib import admin
from .models import Employee,EmployeeAdmin

admin.site.register(Employee,EmployeeAdmin)
```

## OUTPUT
![Admin_interface](https://user-images.githubusercontent.com/119405038/209980350-e20b3d62-ac61-468f-a65e-7401525dc1ae.png)

### Verifying primary key
![Admin_Primarykey](https://user-images.githubusercontent.com/119405038/209980357-c95a7333-2532-4950-9bb3-812b65d225f1.png)


## RESULT
