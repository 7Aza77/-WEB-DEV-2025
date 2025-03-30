from django.shortcuts import render
from .models import Student

def s_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
# Create your views here.
