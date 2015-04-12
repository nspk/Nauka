from django.views.generic import ListView, DetailView

from .models import Termometr

class TermometrListView(ListView):
    model = Termometr

#robie test2