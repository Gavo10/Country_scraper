<#
Setup script for Windows PowerShell:
- creates a virtual environment `venv`
- activates it
- installs dependencies from `requirements.txt`
- runs migrations and optionally runs the scraper

Usage (PowerShell):
  .\setup.ps1 [-CreateDb]

If you pass -CreateDb the script will try to create the Postgres DB `scraping` using psql
with user `postgres` (it will prompt for a password unless you set the PGPASSWORD env var).
#>

param(
    [switch]$CreateDb,
    [switch]$RunScraper
)

Write-Host "== Setup Country Scraper Project =="

if (-not (Test-Path -Path .\venv -PathType Container)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
} else {
    Write-Host "Virtual environment already exists."
}

Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if ($CreateDb) {
    Write-Host "Attempting to create PostgreSQL database 'scraping' (requires psql in PATH)..."
    try {
        # This will ask for password if needed. You can set $env:PGPASSWORD prior to running the script.
        psql -U postgres -c "CREATE DATABASE scraping;"
    } catch {
        Write-Warning "Could not create DB automatically. Create database 'scraping' manually or ensure psql is in PATH and credentials are correct."
    }
}

Write-Host "Applying migrations..."
.\venv\Scripts\python.exe manage.py migrate

Write-Host "(Optional) Create a superuser with:`manage.py createsuperuser`"
if ($RunScraper) {
    Write-Host "Running scraper to populate initial data..."
    .\venv\Scripts\python.exe manage.py scrapecountries
}

Write-Host "Setup complete. Run the server with: .\venv\Scripts\python.exe manage.py runserver"
