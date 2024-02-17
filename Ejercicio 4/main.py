import requests
from datetime import datetime

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate"]
        return bitcoin_price
    except requests.RequestException as e:
        raise Exception(f"Error al consultar la API de Bitcoin: {e}")

def save_price_to_file(price, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a') as file:
        file.write(f"{timestamp}: {price}\n")

def main():
    try:
        bitcoin_price = get_bitcoin_price()
        filename = "bitcoin_prices.txt"
        save_price_to_file(bitcoin_price, filename)
        print("Datos de precio de Bitcoin almacenados en el archivo bitcoin_prices.txt.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
