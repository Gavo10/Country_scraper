Instrucciones rápidas para dejar y ejecutar el proyecto desde cero

1) Crear entorno (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Crear la base de datos PostgreSQL `scraping` y usuario (si no la tienes)

- Desde psql o PgAdmin crea la DB `scraping` y un usuario con password. En `settings.py` está configurado para `postgres` / `1234`.

3) Ejecutar migraciones

```powershell
.\venv\Scripts\python.exe manage.py migrate
```

4) Ejecutar scraper (poblar datos)

```powershell
.\venv\Scripts\python.exe manage.py scrapecountries
```

5) Ejecutar servidor

```powershell
.\venv\Scripts\python.exe manage.py runserver
# Abrir http://127.0.0.1:8000/paises/
```

Notas
- Si vas a subir a Git, revisa `.gitignore` para excluir `venv/`, `__pycache__/` y archivos locales.
- Si quieres que deje solo `countries/migrations/0001_initial.py` puedo eliminar las migraciones extra y dejar solo esa (me avisas y lo hago).