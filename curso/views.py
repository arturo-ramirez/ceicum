from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso
from .forms import CursoForm

# Create your views here.


class CursoView(LoginRequiredMixin, generic.ListView):
    model = Curso
    template_name = 'curso/curso_lista.html'
    context_object_name = "obj"
    login_url = 'common:login'


class CursoNew(LoginRequiredMixin, generic.CreateView):
    model = Curso
    template_name = "curso/curso_form.html"
    context_object_name = "obj"
    form_class = CursoForm
    success_url = reverse_lazy("curso:curso_lista")
    login_url = 'common:login'
    success_message = "Curso creado"


class CursoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Curso
    template_name = "curso/curso_form.html"
    context_object_name = "obj"
    form_class = CursoForm
    success_url = reverse_lazy("curso:curso_lista")
    login_url = 'common:login'
    success_message = "Categoría Actualizada Satisfactoriamente"


class CursoDel(LoginRequiredMixin, generic.DeleteView):
    model = Curso
    template_name = "curso/curso_delete.html"
    context_object_name = "obj"
    form_class = CursoForm
    success_url = reverse_lazy("curso:curso_lista")
    login_url = 'common:login'
    success_message = "Curso eliminado"
