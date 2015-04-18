from django.views.generic import ListView, DetailView

from .models import Termometr, Odczyt

class TermometrListView(ListView):
    model = Termometr

class TermometrDetailView(DetailView):
    model = Termometr

class OdczytListView(ListView):
    model = Odczyt