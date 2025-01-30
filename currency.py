import requests

API_KEY = 'fca_live_PgbmNgFuf67tIUJ6wDOCmNoWTm8SbcVJPnnAScQ1'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "CNY", "AUD", "BRL"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Sorry, we dont have this currency yet.")
        return None

while True:
    base = input("Enter the base currency (press q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")