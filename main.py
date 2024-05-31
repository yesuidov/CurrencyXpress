from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

# a Flask application that converts a user's value in USD to the 
# equivalent value in a specified target currency using real-time 
# exchange rate data fetched from the ExchangeRate-API
@app.route("/convert-currency/<price>/<target_currency>", methods=["GET"])
def get_currency_converter(price, target_currency):
    api_key = "6f2f5d412ca45f64b9d2f641"
    default = "USD"
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{default}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["conversion_rates"][target_currency]

            response_data = {
                "default_currency": data["base_code"],
                "target_currency": target_currency,
                "exchange_rate": exchange_rate,
                "price": price,
                "target_price": int(price) * exchange_rate
            }
            return jsonify(response_data), 200
        else:
            error_msg = {
                "error": "Failed to retrieve info!"
            }
            return jsonify(error_msg), response.status_code
    except Exception as e:
        error_msg = {
            "exception_error": str(e)
        }
        return jsonify(error_msg), 500

if __name__ == "__main__":
    app.run(debug=True)