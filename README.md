# Country Scraper Project
Proyecto Django que extrae datos públicos de países desde `https://www.scrapethissite.com/pages/simple/`, los guarda en PostgreSQL y ofrece una interfaz web para listar, filtrar y borrado lógico (soft-delete).
Estado importante antes de usar
- Las migraciones se han limpiado para este repositorio: en `countries/migrations/` solo debe quedar `__init__.py` y `0001_initial.py`. Asegúrate de no añadir migraciones intermedias extra al hacer cambios si quieres mantener el historial reducido.
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

Archivos y comandos relevantes
- `countries/scraper.py` — lógica de scraping y guardado.
- `countries/management/commands/scrapecountries.py` — comando para ejecutar el scraper desde `manage.py`.
- `countries/models.py` — modelo `Pais` con borrado lógico (`is_deleted`, `deleted_at`).
- `countries/templates/countries/paises_list.html` — plantilla pública con filtros y botón para invocar el scraper.

Uso de `setup.ps1` (Windows)

El proyecto incluye `setup.ps1` para automatizar gran parte del setup local. Ejemplos:

```powershell
# Crear venv, instalar dependencias y aplicar migraciones
.\setup.ps1

# Crear DB (si quieres que intente crearla con psql) y ejecutar el scraper
.\setup.ps1 -CreateDb -RunScraper
```

Git / despliegue

Si quieres inicializar el repositorio Git y subirlo a GitHub, puedes hacerlo así:

```powershell
# Country Scraper Project

This Django project scrapes country data from `https://www.scrapethissite.com/pages/simple/`, stores it in PostgreSQL, and provides a UI to view, filter, and soft-delete records.

Getting started

- Ensure you have Python 3.11+, PostgreSQL, and `virtualenv` installed.
- Create and activate the virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Configure your Postgres connection in `country_scraper/settings.py` (DATABASES section).
- Apply migrations:

```powershell
.\venv\Scripts\python.exe manage.py makemigrations
.\venv\Scripts\python.exe manage.py migrate
```

- Run the scraper from the command line (optional) or via the web UI:

CLI:
```powershell
.\venv\Scripts\python.exe manage.py scrape_countries
```

Web UI:
```powershell
.\venv\Scripts\python.exe manage.py runserver
# Then open http://127.0.0.1:8000/ in your browser
```

Files of interest

- `countries/scraper.py` — scraping and upsert logic used by both the view and management command.
- `countries/views.py` — list, filtering and soft-delete views.
- `countries/templates/countries/country_list.html` — UI, includes a button to trigger scraping.
- `database_schema.sql` — SQL schema and sample data for manual DB setup or inspection.

Deploy / GitHub

- Commit your project to a GitHub repository and share the URL. Example:

```powershell
# Inicializar repo localmente
git init
git add .
git commit -m "Initial commit: cleaned migrations, add scraper and setup script"

# Añadir remote y subir (sustituye la URL con la tuya)
# git remote add origin https://github.com/<tu-usuario>/country_scraper_project.git
# git push -u origin main
```

git add .
git commit -m "Initial scraper app"
git remote add origin https://github.com/<your-username>/country_scraper_project.git
git push -u origin main
```

If you want, I can prepare the GitHub repo and push these files for you (I will need your repo access or to work with a remote URL you provide).
