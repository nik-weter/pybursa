from django.contrib import admin
from django.db import models
from django.forms import widgets
from django import forms

from .models import Student
# Register your models here.

# class StudentAdminForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         widgets = {
#           'by_admin':forms.RadioSelect
#         }

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','email', 'get_courses', 'package')
    ordering = ('package', 'name')
    search_fields = ('name', 'email')
    list_filter = ['email', 'courses__start']
    formfield_overrides = {
        models.ManyToManyField:
            {
                'widget': widgets.CheckboxSelectMultiple
            },
    }
    radio_fields = {"package": admin.HORIZONTAL}
admin.site.register(Student, StudentAdmin)