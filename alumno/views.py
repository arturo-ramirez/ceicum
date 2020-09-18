from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alumno
from .forms import AlumnoForm

import random

# Create your views here.


class AlumnoView(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = "alumno/alumno_lista.html"
    context_object_name = "obj"
    login_url = 'common:login'


class AlumnoNew(LoginRequiredMixin, generic.CreateView):
    model = Alumno
    template_name = "alumno/alumno_form.html"
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("alumno:alumno_lista")
    login_url = 'common:login'
    success_message = "Registro agregado"


class AlumnoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Alumno
    template_name = "alumno/alumno_form.html"
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("alumno:alumno_lista")
    login_url = 'common:login'
    success_message = "Registro actualizado"


class AlumnoDelete(LoginRequiredMixin, generic.DeleteView):
    model = Alumno
    template_name = "alumno/alumno_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("alumno:alumno_lista")


def codigo(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'alumno/password.html', {'password': thepassword})
