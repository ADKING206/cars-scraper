thonimport json
import os
from modules.fetcher import fetch_car_listings
from modules.parser import parse_listing_data
from modules.exporter import export_data
from utils.logger import log_info, log_error

def main():
    try:
        log_info("Starting Cars.com scraper")
        
        input_urls = load_input_urls('data/input_urls.txt')
        if not input_urls:
            raise ValueError("No URLs found for scraping.")
        
        listings = fetch_car_listings(input_urls)
        parsed_data = parse_listing_data(listings)
        export_data(parsed_data, 'data/sample_output.json')
        
        log_info("Scraping completed successfully.")
    except Exception as e:
        log_error(f"An error occurred: {e}")

def load_input_urls(file_path):
    if not os.path.exists(file_path):
        log_error(f"Input file {file_path} not found.")
        return []
    with open(file_path, 'r') as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()