from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.


class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = 'common/index.html'
    login_url = 'common:login'
