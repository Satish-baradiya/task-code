from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    teachers = models.ManyToManyField(Teacher, related_name="students")

    def __str__(self):
        return self.name
