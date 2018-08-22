from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Course

from .forms import CourseForm, CourseCustomForm


# Create your views here.
class CoursesList(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(CoursesList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['courses'] = Course.objects.all()
        return context

    #def get_queryset(self):
    #    return Course.objects.all()


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


def course_view(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/detail.html', {'course': course})

class CourseView(FormView):
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    form_class = CourseForm
    success_url = '/courses/'


    def form_valid(self, form):
        form.save()
        return super(CourseView, self).form_valid()


class CourseEdit(UpdateView):
    model = Course
    context_object_name = 'course'
    form_class = CourseForm
    template_name = 'courses/edit.html'
    success_url = '/courses/'

def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('course_edit', course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/edit.html',
                  {'form': form, 'course': course})

class CourseCreate(CreateView):
    model = Course
    context_object_name = 'course'
    form_class = CourseForm
    template_name = 'courses/add.html'
    success_url = '/courses/'

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            print('is valid')
            course = form.save()
            return redirect('courses:detail', course.id)
        else:
            print('no valid')
    else:
        form = CourseForm()
        course = ''
    return render(request, 'courses/add.html',
                  {'form': form, 'course': 'course'})

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    #template_name = 'courses/list.html'