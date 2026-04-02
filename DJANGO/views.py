from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.filter()
    return render(request,'STUDENTS/home.html',{
        'students':students
    })