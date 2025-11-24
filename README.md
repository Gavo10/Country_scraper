# Country Scraper Project
Proyecto Django que extrae datos públicos de países desde `https://www.scrapethissite.com/pages/simple/`, los guarda en PostgreSQL y ofrece una interfaz web para listar, filtrar y borrado lógico.

Requisitos
- Python 3.11+ (o una versión compatible con tu entorno)
- PostgreSQL
- `psql` en PATH (opcional, para creación automática de la DB)
Instalación y puesta en marcha (Windows PowerShell)

1) Crear y activar el entorno virtual e instalar dependencias:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

2) (Opcional) Crear la base de datos PostgreSQL `scraping` desde PowerShell si tienes `psql`:

```powershell
# Establece la variable si no quieres que pida contraseña interactiva
#$env:PGPASSWORD = "1234"
psql -U postgres -c "CREATE DATABASE scraping;"
```

3) Aplicar migraciones:

```powershell
.\venv\Scripts\python.exe manage.py migrate
```

4) (Opcional) Poblar datos iniciales ejecutando el scraper desde CLI:

```powershell
.\venv\Scripts\python.exe manage.py scrapecountries
```

5) Ejecutar servidor de desarrollo:

```powershell
.\venv\Scripts\python.exe manage.py runserver
# Abrir http://127.0.0.1:8000/paises/ para ver la lista pública
```

Uso de `setup.ps1` (Windows)

El proyecto incluye `setup.ps1` para automatizar gran parte del setup local. Ejemplos:

```powershell
# Crear venv, instalar dependencias y aplicar migraciones
.\setup.ps1

# Crear DB (si quieres que intente crearla con psql) y ejecutar el scraper
.\setup.ps1 -CreateDb -RunScraper
```

