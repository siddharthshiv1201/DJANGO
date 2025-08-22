# records/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True) # Roll number unique hona chahiye
    student_class = models.CharField(max_length=10)

    def __str__(self):
        return self.name