# records/admin.py

from django.contrib import admin
from .models import Student

# Student model ko admin site par register karein
admin.site.register(Student)