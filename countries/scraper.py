import requests
from bs4 import BeautifulSoup
from countries.models import Pais

def scrape_and_save_countries():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    countries_divs = soup.find_all("div", class_="country")
    for div in countries_divs:
        nombre = div.find("h3", class_="country-name").get_text(strip=True)
        capital = div.find("span", class_="country-capital").get_text(strip=True)
        poblacion = int(div.find("span", class_="country-population").get_text(strip=True))
        area = float(div.find("span", class_="country-area").get_text(strip=True))
        Pais.objects.get_or_create(
            nombre=nombre,
            capital=capital,
            poblacion=poblacion,
            area=area
        )

if __name__ == "__main__":
    scrape_and_save_countries()
