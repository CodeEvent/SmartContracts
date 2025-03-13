import pandas as pd
from src.cost_comparison import compare_costs

def test_compare_costs():
    gas_data = pd.read_csv("data/ethereum_gas_data.csv")
    paypal_data = pd.read_csv("data/paypal_transaction_data.csv")
    
    result = compare_costs(gas_data, paypal_data)
    assert isinstance(result, dict)
    assert 'savings' in result
