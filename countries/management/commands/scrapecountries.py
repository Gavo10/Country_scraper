from django.core.management.base import BaseCommand
from countries.scraper import scrape_and_save_countries

class Command(BaseCommand):
    help = 'Scrapea países y los guarda en la tabla "paises"'

    def handle(self, *args, **kwargs):
        scrape_and_save_countries()
        self.stdout.write(self.style.SUCCESS('Scraping completado y datos guardados en la tabla "paises".'))
