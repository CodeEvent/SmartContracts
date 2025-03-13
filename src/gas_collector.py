# gas_collector.py

import logging
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_gas_data():
    """
    Fetch gas data from the Etherscan API.
    """
    url = "https://api.etherscan.io/api"
    params = {
        "module": "gastracker",
        "action": "gasoracle",
        "apikey": "YRUWP747YUS4D3VDZHZQBKNS5C6QXKGFD1"
    }
    
    try:
        logging.debug("Starting new HTTPS connection (1): api.etherscan.io:443")
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check if the request was successful
        
        # Log the response to ensure we have data
        logging.debug(f"Response data: {response.text}")
        
        gas_data = response.json()
        
        # Check if the API returned the expected data
        if gas_data and gas_data.get("status") == "1":
            return gas_data["result"]
        else:
            logging.error("Failed to fetch valid gas data.")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None

def evaluate_smart_contract_costs(gas_data):
    if gas_data is None:
        logging.error("Gas data is None. Cannot evaluate transaction costs.")
        return None
    
    # Extract relevant gas prices for smart contract transactions
    safe_gas_price = float(gas_data['SafeGasPrice'])
    propose_gas_price = float(gas_data['ProposeGasPrice'])
    fast_gas_price = float(gas_data['FastGasPrice'])
    
    transaction_costs = {
        "SafeGasPrice": safe_gas_price,
        "ProposeGasPrice": propose_gas_price,
        "FastGasPrice": fast_gas_price,
    }
    logging.info(f"Transaction Costs Analysis: {transaction_costs}")
    return transaction_costs

def get_traditional_costs():
    """
    Placeholder function to return traditional transaction costs.
    Replace this with actual data when available.
    """
    return {
        "SafeGasPrice": 1.0,
        "ProposeGasPrice": 1.2,
        "FastGasPrice": 1.5
    }

def compare_transaction_costs(smart_contract_costs, traditional_costs):
    comparison = {}
    
    for key in smart_contract_costs:
        if key in traditional_costs:
            comparison[key] = {
                'SmartContractCost': smart_contract_costs[key],
                'TraditionalCost': traditional_costs[key],
                'Difference': traditional_costs[key] - smart_contract_costs[key],
                'PercentageDifference': ((traditional_costs[key] - smart_contract_costs[key]) / traditional_costs[key]) * 100
            }
    
    return comparison

def save_to_csv(smart_contract_costs, traditional_costs, comparison):
    """
    Save the gas price analysis, traditional costs, and comparison to a CSV file.
    """
    import csv
    
    filename = "gas_prices_analysis.csv"
    fields = ["CostType", "SmartContractCost", "TraditionalCost", "Difference", "PercentageDifference"]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        
        for key in comparison:
            writer.writerow([
                key,
                comparison[key]['SmartContractCost'],
                comparison[key]['TraditionalCost'],
                comparison[key]['Difference'],
                comparison[key]['PercentageDifference']
            ])

def main():
    logging.debug("Fetching gas prices...")
    gas_data = fetch_gas_data()  # Fetch gas prices
    
    if gas_data is None:
        logging.error("No gas data fetched. Exiting the program.")
        return
    
    smart_contract_costs = evaluate_smart_contract_costs(gas_data)
    
    if smart_contract_costs:
        traditional_costs = get_traditional_costs()
        comparison = compare_transaction_costs(smart_contract_costs, traditional_costs)
        
        logging.info(f"Transaction Costs Comparison: {comparison}")
        save_to_csv(smart_contract_costs, traditional_costs, comparison)

if __name__ == "__main__":
    main()
