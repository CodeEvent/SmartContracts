def analyze_transaction_costs(eth_prices, paypal_fee):
    eth_low, eth_medium, eth_high = eth_prices
    
    # Example calculation of cost efficiency (could be more complex)
    eth_cost = min(eth_low, eth_medium, eth_high)  # Using lowest gas price for comparison
    cost_savings = paypal_fee - eth_cost  # Assuming the Paypal fee is in USD, and ETH price is in Gwei
    
    print(f"Ethereum Transaction Cost: {eth_cost} Gwei")
    print(f"PayPal Transaction Fee: {paypal_fee} USD")
    print(f"Potential Savings: {cost_savings} USD")
    return cost_savings
