from flask import Flask
import os
from dotenv import load_dotenv
import requests
from constants import BASE_PATH
from flask import jsonify
from cache import get_stock_price_from_cache, set_stock_price_in_cache

app = Flask(__name__)

# Route to get the stock price for a given stock symbol
@app.route("/get-price/<symbol>", methods=["GET"])
def get_stock_price(symbol):
    base_url = BASE_PATH + "v3/profile/"

    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400
    try:
        stock_price_from_cache = get_stock_price_from_cache(symbol)
        if stock_price_from_cache:
            return jsonify({"symbol": symbol, "price": stock_price_from_cache})
        
        response = requests.get(f"{base_url}{symbol}", params={"apikey": os.getenv("API_KEY")}, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("Request data" + base_url + symbol)
        

        if data:
            price = data[0].get("price")
            print(price)
            set_stock_price_in_cache(symbol, price)
            return jsonify({"symbol": symbol, "price": price})
        else:
            return jsonify({"error": "Stock symbol not found"}), 404

    except requests.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    print(f"API Key: {api_key}")
    app.run(port=5000)

