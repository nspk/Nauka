from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Termometr

class TermometrListView(ListView):
    model = Termometr