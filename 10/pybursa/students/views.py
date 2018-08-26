from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .models import *
from .forms import StudentForm, MailCustomForm
from coaches.models import Coache




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

class MailView(FormView):
    template_name = 'students/email.html'
    form_class = MailCustomForm
    success_url = '/students/send/'

    # def form_valid(self, form):
    #     message = "{name} / {email} said: ".format(
    #         name=form.cleaned_data.get('name'),
    #         email=form.cleaned_data.get('email'))
    #     message += "\n\n{0}".format(form.cleaned_data.get('message'))
    #     send_mail(
    #         subject=form.cleaned_data.get('subject').strip(),
    #         message=message,
    #         from_email='contact-form@myapp.com',
    #         recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
    #     )
    #     return super(MailView, self).form_valid(form)
    def form_valid(self, form):
        print(form.cleaned_data)
        subject = form.cleaned_data['theme']
        coach = form.cleaned_data['coach']
        goal = form.cleaned_data['goal']
        text = form.cleaned_data['text']
        messege = 'Достопочтенный и многоуважаемый {}!' \
                  'Спешу уведомить Вас о неподобающем поведении студента {}. Дело в следующем.' \
                  '{}. С уважением, один из Ваших студентов'.format(coach, goal, text)
        form.send_email(
            subject = subject,
            message = messege,
            from_email = form.cleaned_data['email'],
            address = coach
        )
        #form.send_email()
        return super(MailView, self).form_valid(form)

