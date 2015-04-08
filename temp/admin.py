from django.contrib import admin
from .models import Termometr, Odczyt

class TermometrAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['nazwa', 'datadodania', 'dodanyprzez']

class OdczytAdmin(admin.ModelAdmin):
    search_fields = ['odczyt']
    list_display = ['odczyt', 'termometr', 'data']

admin.site.register(Termometr, TermometrAdmin)
admin.site.register(Odczyt, OdczytAdmin)