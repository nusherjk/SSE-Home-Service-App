from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'landing.html'


class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'Dashboard.html'