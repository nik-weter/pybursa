from django.urls import reverse
from django.db import models
from django import forms

from courses.models import Course, Address
# Create your models here.
class Student(models.Model):
    PACKAGE_CHOICES = (
        ('s', 'Standard'),
        ('g', 'Gold'),
        ('p', 'Platinum')
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
    package = models.CharField(max_length=30, choices=PACKAGE_CHOICES, default='s')
    #package = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.RadioSelect)

    def get_courses(self):
        return "\n".join([p.name for p in self.courses.all()])

    def get_absolute_url(self):
        return reverse('list', kwargs={'pk': self.pk})