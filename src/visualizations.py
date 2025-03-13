import matplotlib.pyplot as plt

def plot_gas_prices(eth_prices, paypal_fee):
    eth_low, eth_medium, eth_high = eth_prices

    # Plot Ethereum gas prices and PayPal fee comparison
    categories = ['Low', 'Medium', 'High']
    eth_prices = [eth_low, eth_medium, eth_high]

    plt.plot(categories, eth_prices, label="Ethereum Gas Prices (Gwei)", color='blue', marker='o')
    plt.axhline(y=paypal_fee, color='red', linestyle='--', label=f"PayPal Fee: {paypal_fee} USD")

    plt.xlabel("Gas Price Categories")
    plt.ylabel("Price (in Gwei / USD)")
    plt.title("Ethereum Gas Prices vs PayPal Transaction Fee")
    plt.legend()

    plt.show()
