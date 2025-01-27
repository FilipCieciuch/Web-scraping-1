import requests
from bs4 import BeautifulSoup
import csv

# URL strony
url = "https://johansen-ias.pl/terapeuci/"

# Pobranie zawartości strony
response = requests.get(url)
if response.status_code != 200:
    print(f"Błąd podczas pobierania strony: {response.status_code}")
    exit()

# Parsowanie HTML za pomocą BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Znajdź sekcję z miastami
cities = soup.select('.elementor-accordion-item')

# Wynikowa tabela
specialists_data = []

for city in cities:
    # Nazwa miasta
    city_name_element = city.select_one('.elementor-tab-title a.elementor-accordion-title')
    if city_name_element:
        city_name = city_name_element.text.strip()
    else:
        continue

    # Pobranie szczegółowych informacji o specjalistach
    content_element = city.select_one('.elementor-tab-content')
    if content_element:
        paragraphs = content_element.find_all('p')
        for i in range(0, len(paragraphs), 3):
            try:
                # Imię i nazwisko
                name = paragraphs[i].text.strip() if name != '\u00A0' else ""
                # E-mail (jeśli istnieje)
                email = paragraphs[i + 1].text.strip() if i + 1 < len(paragraphs) and '@' in paragraphs[i + 1].text else ""
                # Numer telefonu (jeśli istnieje)
                phone = paragraphs[i + 2].text.strip() if i + 2 < len(paragraphs) and any(char.isdigit() for char in paragraphs[i + 2].text) else ""
                # Dodanie danych specjalisty
                specialists_data.append((name, email, phone, city_name))
            except IndexError:
                continue

# Wypisanie danych do konsoli
print("Imię i nazwisko | E-mail | Telefon | Miasto")
print("-" * 50)
for specialist in specialists_data[:50]:
    print(" | ".join(specialist))

# # Zapisanie danych do pliku CSV
# output_file = "D:\Python\Web scraping 1\specialists_data.csv"
# with open(output_file, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Imię i nazwisko", "E-mail", "Telefon", "Miasto"])
#     writer.writerows(specialists_data)

# print(f"Dane zapisano do pliku {output_file}")
