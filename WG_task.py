import requests
from bs4 import BeautifulSoup
import csv
import re

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
city_data = []
# cities = cities[:5]


for city in cities:
    # Nazwa miasta
    city_name_element = city.select_one('.elementor-tab-title a.elementor-accordion-title')
    if city_name_element:
        city_name = city_name_element.text.strip()
    else:
        continue

    # Znalezienie liczby ośrodków na podstawie imion i nazwisk specjalistów
    content_element = city.select_one('.elementor-tab-content')
    if content_element:
        specialists = content_element.find_all('p', recursive=False)
        number_of_centers = 0
        for specialist in specialists:
            # Check if the string contains phone number
            # pattern1 = r'\d{3} \d{3} \d{3}'
            pattern = r'\d{3}(?: |\u00A0)\d{3}(?: |\u00A0)\d{3}'

            # match1 = re.search(pattern1, specialist.text)
            match = re.search(pattern, specialist.text)
            if match:
                number_of_centers += 1
                # print("long number in:", specialist)
            else:
                pattern = r'\d{3}(?: |\u00A0)'
                match = re.search(pattern, specialist.text)
                if match:
                    number_of_centers += 1
                    # print("short number in:", specialist)          
                

    else:
        number_of_centers = 0

    # Dodanie danych do tabeli
    city_data.append((city_name, number_of_centers))

# Wyświetlenie wyników
# print("Miasto\tLiczba ośrodków")
# for city_name, number_of_centers in city_data:
#     print(f"{city_name}\t{number_of_centers}")

# Zapisanie danych do pliku CSV

output_file = "D:\Python\Web scraping 1\city_centers.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Miasto", "Liczba ośrodków"])
    writer.writerows(city_data)

print(f"Dane zapisano do pliku {output_file}")


