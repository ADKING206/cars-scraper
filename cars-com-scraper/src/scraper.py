thonimport requests
from bs4 import BeautifulSoup
import json
import csv
import os

class CarsScraper:
    def __init__(self, url, output_format='json'):
        self.url = url
        self.output_format = output_format
        self.data = []

    def fetch_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        listings = soup.find_all('div', class_='listing')
        for listing in listings:
            car_data = {
                "list_url": [self.url],
                "record_url": listing.find('a')['href'],
                "name": listing.find('h2').text.strip(),
                "description": listing.find('p', class_='description').text.strip() if listing.find('p', class_='description') else '',
                "mileage": listing.find('div', class_='mileage').text.strip() if listing.find('div', class_='mileage') else '',
                "price": listing.find('span', class_='price').text.strip(),
                "make": listing.find('span', class_='make').text.strip(),
                "model": listing.find('span', class_='model').text.strip(),
                "trim": listing.find('span', class_='trim').text.strip() if listing.find('span', class_='trim') else '',
                "year": listing.find('span', class_='year').text.strip(),
                "vin": listing.find('span', class_='vin').text.strip() if listing.find('span', class_='vin') else '',
                "body": listing.find('span', class_='body').text.strip() if listing.find('span', class_='body') else '',
                "cylinders": listing.find('span', class_='cylinders').text.strip() if listing.find('span', class_='cylinders') else '',
                "doors": listing.find('span', class_='doors').text.strip() if listing.find('span', class_='doors') else '',
                "drivetrain": listing.find('span', class_='drivetrain').text.strip() if listing.find('span', class_='drivetrain') else '',
                "exterior_color": listing.find('span', class_='exterior-color').text.strip() if listing.find('span', class_='exterior-color') else '',
                "interior_color": listing.find('span', class_='interior-color').text.strip() if listing.find('span', class_='interior-color') else '',
                "fuel": listing.find('span', class_='fuel').text.strip() if listing.find('span', class_='fuel') else '',
                "transmission": listing.find('span', class_='transmission').text.strip() if listing.find('span', class_='transmission') else '',
                "engine": listing.find('span', class_='engine').text.strip() if listing.find('span', class_='engine') else '',
                "stock_number": listing.find('span', class_='stock-number').text.strip() if listing.find('span', class_='stock-number') else '',
                "features": [feature.text.strip() for feature in listing.find_all('li', class_='feature')],
                "images": [img['src'] for img in listing.find_all('img', class_='car-image')],
            }
            self.data.append(car_data)

    def export_data(self):
        if self.output_format == 'json':
            with open('output.json', 'w') as outfile:
                json.dump(self.data, outfile, indent=4)
        elif self.output_format == 'csv':
            keys = self.data[0].keys()
            with open('output.csv', 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.data)
        elif self.output_format == 'excel':
            import pandas as pd
            df = pd.DataFrame(self.data)
            df.to_excel('output.xlsx', index=False)

if __name__ == '__main__':
    scraper = CarsScraper(url='https://www.cars.com/shopping/results/')
    scraper.fetch_data()
    scraper.export_data()