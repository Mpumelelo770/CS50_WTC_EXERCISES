import requests
import json
import sys

key = "de3bfa2632b1304eedbca4ee89ef296e2014c832b1005ff50b118b16f3242866"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={key}"


response = requests.get(url)

bitcoin = response.json()
bitcoin_data = bitcoin["data"]
price_usd = bitcoin_data["priceUsd"]



try:
    bitcoins = float(price_usd) * float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")



print(f"${bitcoins:,.4f}")
