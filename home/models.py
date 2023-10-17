from django.db import models
import django

# Create your models here.


class Student(models.Model):
    # id = models.AutoField() Django adds this field Automatically
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    image = models.ImageField()


class Course(models.Model):
    pass
