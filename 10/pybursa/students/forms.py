from django import forms

from .models import Student

from courses.models import Course, Address

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