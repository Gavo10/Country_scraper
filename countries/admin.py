from django.contrib import admin
from .models import Pais

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capital', 'poblacion', 'area')
    search_fields = ('nombre', 'capital')
