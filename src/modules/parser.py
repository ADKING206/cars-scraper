thonfrom bs4 import BeautifulSoup

def parse_listing_data(html_data):
    parsed_data = []
    for page_content in html_data:
        soup = BeautifulSoup(page_content, 'html.parser')
        cars = extract_car_details(soup)
        parsed_data.extend(cars)
    return parsed_data

def extract_car_details(soup):
    cars = []
    for listing in soup.find_all('div', class_='listing'):
        car = {
            'name': listing.find('h2').get_text(),
            'price': listing.find('span', class_='price').get_text(),
            'mileage': listing.find('span', class_='mileage').get_text(),
            'year': listing.find('span', class_='year').get_text(),
            'make': listing.find('span', class_='make').get_text(),
            'model': listing.find('span', class_='model').get_text(),
        }
        cars.append(car)
    return cars