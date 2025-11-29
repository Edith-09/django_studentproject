from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    reg_no=models.CharField(max_length=50)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    
    def __str__(self):
        return self.name
