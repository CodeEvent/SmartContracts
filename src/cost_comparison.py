import requests

def get_eth_gas_prices():
    url = "https://api.example.com/gas"  # Replace with the actual Ethereum gas price API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data['Low'], data['Medium'], data['High']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Ethereum gas prices: {e}")
        return None

def get_paypal_transaction_fee():
    # Make a request to PayPal API (ensure to set up your API credentials)
    url = "https://api.paypal.com/v1/transactions/fees"
    headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure no errors with the request
        return response.json()  # Return the data from PayPal API
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PayPal transaction fees: {e}")
        return None

def compare_transaction_costs():
    # Fetch Ethereum gas prices
    eth_prices = get_eth_gas_prices()
    if not eth_prices:
        print("Error: Could not fetch Ethereum gas prices.")
        return

    # Fetch PayPal transaction fees
    paypal_data = get_paypal_transaction_fee()
    if not paypal_data:
        print("Error: Could not fetch PayPal transaction fees.")
        return

    eth_low, eth_medium, eth_high = eth_prices
    paypal_fee = paypal_data['transaction_fee']  # Example, adjust based on PayPal API response structure
    
    print(f"Ethereum Gas Price (Low): {eth_low} Gwei")
    print(f"Ethereum Gas Price (Medium): {eth_medium} Gwei")
    print(f"Ethereum Gas Price (High): {eth_high} Gwei")
    print(f"PayPal Transaction Fee: {paypal_fee} USD")

# Call the function to compare costs
compare_transaction_costs()
