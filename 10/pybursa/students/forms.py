from django import forms
from django.core.mail import send_mail

from .models import Student

from courses.models import Course, Address
from coaches.models import Coache

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'surname', 'date_of_birth', 'email', 'phone', 'courses', 'package')
        widgets = {
            'package': forms.RadioSelect
        }

# class StudentCustomForm(forms.Form):
#     PACKAGE_CHOICES = (
#         ('s', 'Standard'),
#         ('g', 'Gold'),
#         ('p', 'Platinum')
#     )
#     name = forms.CharField(max_length=255)
#     surname = forms.CharField(max_length=255)
#     date_of_birth = forms.DateField()
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=30)
#     courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
#     package = forms.ChoiceField(widget=forms.RadioSelect, choices=PACKAGE_CHOICES)

class MailCustomForm(forms.Form):
    theme = forms.CharField(max_length=255)
    coach = forms.ModelChoiceField(queryset=Coache.objects.all())
    goal = forms.ModelChoiceField(queryset=Student.objects.all())
    text = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def send_email(self, subject, message, from_email, address):
    # def send_email(self):
    #     #address_list = Coache.objects.get(id = address)
        address_list = ['nik-weter@yandex.ru']
    #     subject =self.theme
    #     coach = self.coach
    #     goal = self.goal
    #     text = self.text
    #     from_email = self.email
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=address_list)