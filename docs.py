from flask import Flask, request, jsonify
# import pandas as pd
import json
import random

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    """
    This function receives a POST request with 15 files, and stores them in a local folder. 
    And returns a dummy json response.
    """
    # files = request.files
    # for file in files:
    #     files[file].save(f'./{file}')


    response = {
    'fcf_values': [random.uniform(100, 1000) for _ in range(5)],
    'terminal_value': "1000",
    'wacc': "3.53%",
    'npv_value': "1234567",
    'equity_value': "1234567",
    'current_market_share_price': random.uniform(10, 100),
    'outstanding_shares': "607 mn",
    'fair_price': "34.67",
    'growth': "267%"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)