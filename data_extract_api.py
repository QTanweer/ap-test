from flask import Flask, request, jsonify
import random


app = Flask(__name__)

@app.route('/financial_data', methods=['POST'])
def get_financial_data():
    data = request.get_json()

    company_name = data.get('company_name')
    ticker_name = data.get('ticker_name')

    # Here you would typically call a function or a service that fetches the required data
    # For the sake of this example, let's return some dummy data

    response = {
        'Revenue Growth Rate': '10%',
        'Tax shield': '15%',
        'Expenses Growth Rate': '5%',
        'Depreciation and Amortization': '20%',
        'EBITDA': '25%',
        'Equity Risk Premium': '',
        'Risk Free Rate': '2.3%',
        'Beta': '0.89',
        'Current Market Share Price': '103.5',
        'Outstanding Shares': '80M',
        'EV/EBITDA Multiple': '20'
    }

    return jsonify(response)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Here you would typically call a function or a service that calculates the required data
    # For the sake of this example, let's return some dummy data

    response = {
    'FCF Values': [random.uniform(100, 1000) for _ in range(5)],
    'Terminal Value': "1000",
    'WACC': "3.53%",
    'NPV Value': "1234567",
    'Equity Value': "1234567",
    'Current Market Share Price': random.uniform(10, 100),
    'Outstanding Shares': "607 mn",
    'Fair Price': "34.67",
    'Growth': "267%"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080 ,debug=True)