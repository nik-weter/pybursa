from django.shortcuts import render, redirect
from .models import *
from .forms import StudentForm

# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})


def student_view(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/single.html', {'student': student})


def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_list', student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html',
                  {'form': form, 'student': student})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('is valid')
            student = form.save()
            return redirect('students:detail', student.id)
        else:
            print('no valid')
    else:
        form = StudentForm()
        student = ''
    return render(request, 'students/add.html',
                  {'form': form, 'student': 'student'})


def student_delete(request, student_id):
    Student.objects.get(id=student_id).delete()

    return redirect('students:list')