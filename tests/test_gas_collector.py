import logging
import requests
import json

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_gas_data():
    url = "https://api.example.com/gas"  # Replace with your actual URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        logging.info("Successfully fetched gas data")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching gas data: {e}")
        return None

if __name__ == "__main__":
    data = fetch_gas_data()
    if data:
        print(f"Low: {data['Low']} Gwei")
        print(f"Medium: {data['Medium']} Gwei")
        print(f"High: {data['High']} Gwei")
