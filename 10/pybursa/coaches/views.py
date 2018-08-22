from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

# Create your views here.

from .models import Coache
from .forms import CoacheForm

# Create your views here.
class CoachesList(ListView):
    model = Coache
    template_name = 'coaches/list.html'

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(CoachesList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['coaches'] = Coache.objects.all()
        return context

# def coaches_list(request):
#     coaches = Coache.objects.all()
#     print(coaches)
#     return render(request, 'coaches/list.html', {'coaches': coaches})

class CoacheDetailView(DetailView):
    model = Coache
    template_name = 'coaches/detail.html'
    context_object_name = 'coache'


def coache_view(request, coache_id):
    coache = get_object_or_404(Coache, id=coache_id)
    return render(request, 'coaches/detail.html', {'coache': coache})

class CoacheView(FormView):
    template_name = 'coaches/edit.html'
    context_object_name = 'coache'
    form_class = CoacheForm
    success_url = '/coaches/'


    def form_valid(self, form):
        form.save()
        return super(CoacheView, self).form_valid()


class CoacheEdit(UpdateView):
    model = Coache
    context_object_name = 'coache'
    form_class = CoacheForm
    template_name = 'coaches/edit.html'
    success_url = '/coaches/'

class CoacheCreate(CreateView):
    model = Coache
    fields = ('name', 'surname', 'email', 'role', 'user', 'dossier')
    # context_object_name = 'coache'
    # form_class = CoacheForm
    template_name = 'coaches/add.html'
    # success_url = reverse_lazy('coaches:list')


def coache_add(request):
    if request.method == 'POST':
        form = CoacheForm(request.POST)
        if form.is_valid():
            print('is valid')
            coache = form.save()
            return redirect('coaches:detail', coache.id)
        else:
            print('no valid')
    else:
        form = CoacheForm()
        coache = ''
    return render(request, 'coaches/add.html',
                  {'form': form, 'coache': 'coache'})

class CoacheDelete(DeleteView):
    model = Coache
    success_url = reverse_lazy('coaches:list')
    #template_name = 'courses/list.html'