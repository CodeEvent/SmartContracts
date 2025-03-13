# Smart Contracts Transaction Cost Analysis

This project analyzes the transaction costs of smart contracts based on real-time Ethereum gas prices. The goal is to determine whether smart contracts reduce transaction costs compared to traditional transaction methods.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Overview

This project fetches real-time gas prices from the Ethereum network using the [Etherscan API](https://etherscan.io/apis). It calculates transaction costs for smart contracts based on different gas price categories (SafeGasPrice, ProposeGasPrice, FastGasPrice). Additionally, the project compares these costs with traditional transaction costs to evaluate whether smart contracts offer cost reduction.

## Features

- Fetches real-time gas prices from Etherscan API.
- Computes transaction costs for different gas price categories.
- Compares smart contract transaction costs with traditional transaction methods.
- Outputs a detailed analysis and comparison.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CodeEvent/SmartContracts.git

2. Navigate to the project directory:
   ```bash
   cd SmartContracts

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Configuration
Obtain an API key from Etherscan for access to the gas price API.
Replace the API_KEY variable in the gas_collector.py script with your Etherscan API key.

## Usage
To run the analysis and fetch transaction costs, use the following command:
python src/gas_collector.py

The output will display the calculated transaction costs for smart contracts and traditional transactions, as well as the comparison between the two.



## Technologies Used
Python 3.x
Requests (for API calls)
JSON (for parsing API responses)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

   
   
