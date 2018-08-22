from django import forms

from .models import Course

from coaches.models import Coache

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('language', 'name', 'detail', 'slug', 'prepod', 'assistent', 'start', 'end', 'venue')
        # widgets = {
        #     'package': forms.RadioSelect
        # }

class CourseCustomForm(forms.Form):
    language = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    detail = forms.TimeField()
    slug = forms.SlugField()
    prepod = forms.ModelMultipleChoiceField(queryset=Coache.objects.all())
    assistent = forms.ModelMultipleChoiceField(queryset=Coache.objects.all())
    start = forms.DateField()
    stop = forms.DateField()