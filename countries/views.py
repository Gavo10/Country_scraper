from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Pais
from .scraper import scrape_and_save_countries
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.db.models import Q


def paises_list(request):
    # filtros recibidos por GET
    q_nombre = request.GET.get('q_nombre', '').strip()
    q_capital = request.GET.get('q_capital', '').strip()
    min_p = request.GET.get('min_poblacion')
    max_p = request.GET.get('max_poblacion')

    qs = Pais.objects.all()

    if q_nombre:
        qs = qs.filter(nombre__icontains=q_nombre)
    if q_capital:
        qs = qs.filter(capital__icontains=q_capital)
    if min_p:
        try:
            qs = qs.filter(poblacion__gte=int(min_p))
        except ValueError:
            pass
    if max_p:
        try:
            qs = qs.filter(poblacion__lte=int(max_p))
        except ValueError:
            pass

    # orden por defecto: alfabético ascendente por 'pais' (definido en Meta)
    paises = qs.order_by('nombre')
    return render(request, 'countries/paises_list.html', {'paises': paises})


@require_POST
def run_scrape(request):
    """Ejecuta el scraping y redirige a la lista de países.

    Protegido por CSRF: el formulario en la plantilla usa POST y `csrf_token`.
    """
    scrape_and_save_countries()
    messages.success(request, 'Scraping ejecutado correctamente.')
    return redirect(reverse('countries:paises_list'))


@require_http_methods(["POST"])
def borrar_pais(request, pk):
    """Borrado lógico: marca `is_deleted=True` y guarda `deleted_at`."""
    pais = get_object_or_404(Pais, pk=pk)
    pais.soft_delete()
    messages.success(request, f'El país "{pais.nombre}" fue eliminado (borrado lógico).')
    return redirect(reverse('countries:paises_list'))

