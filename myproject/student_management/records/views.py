# records/views.py

from django.shortcuts import render
from .models import Student

def student_list(request):
    # Database se saare students fetch karein
    students = Student.objects.all()
    # Data ko template mein bhejein
    return render(request, 'records/student_list.html', {'students': students})