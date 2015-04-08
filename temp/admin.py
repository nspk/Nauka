from django.contrib import admin
from .models import Termometr, Odczyt

class TermometrAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['nazwa', 'datadodania', 'dodanyprzez']

admin.site.register(Termometr, TermometrAdmin)
admin.site.register(Odczyt)