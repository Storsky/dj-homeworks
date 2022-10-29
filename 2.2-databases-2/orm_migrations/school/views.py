from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    context = {'object_list': Student.objects.order_by(ordering)}    
    for student in Student.objects.all():
        for teacher in student.teachers.all():
            print(teacher.name)
    return render(request, template, context)
