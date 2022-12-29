# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram


## DESIGN STEPS

### STEP 1:
Create a django application using ```django-admin startapp <appname>``` in command line.
Head to the application directory created inside the project directory. Open the models.py file.
In models.py create two classes one defining the attributes and the other one defining attribute value types.

### STEP 2:
In the same directory, Head to admins.py and import the two classes from models.py that you have created earlier.
Now register your created models in admins.py file and save both the files

### STEP 3:
Start the Django server and head over to admin page.
Using the admin interface, you can add or delete data in the database


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
Hence a Django application to store and retrieve data from a database using Object Relational Mapping(ORM) is developed.
