import pandas as pd
from src.data_analysis import analyze_data

def test_analyze_data():
    gas_data = pd.read_csv("data/ethereum_gas_data.csv")
    paypal_data = pd.read_csv("data/paypal_transaction_data.csv")
    
    result = analyze_data(gas_data, paypal_data)
    assert 'average_ethereum_cost' in result
    assert 'average_paypal_cost' in result
