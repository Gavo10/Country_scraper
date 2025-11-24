from django.urls import path
from .views import paises_list, run_scrape, borrar_pais

app_name = 'countries'

urlpatterns = [
    path('paises/', paises_list, name='paises_list'),
    path('scrapear/', run_scrape, name='scrapear'),
    path('borrar/<int:pk>/', borrar_pais, name='borrar_pais'),
]
