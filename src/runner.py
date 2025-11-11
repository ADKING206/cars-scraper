thonimport json
from extractors.cars_com_parser import parse_car_data
from outputs.exporters import export_to_csv, export_to_json, export_to_excel
from config.settings import SETTINGS

def run_scraper():
    # Fetch data from the Cars.com website
    car_data = parse_car_data(SETTINGS['url'])

    # Export the data to different formats
    export_to_csv(car_data, 'output.csv')
    export_to_json(car_data, 'output.json')
    export_to_excel(car_data, 'output.xlsx')

if __name__ == "__main__":
    run_scraper()