import pandas as pd
import requests
import time
import json

API_KEY = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your real Etherscan API key

def get_transactions(wallet):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}"
    response = requests.get(url)
    time.sleep(0.2)  # avoid rate limits
    if response.ok:
        return response.json().get('result', [])
    return []

def main():
    wallets = pd.read_csv('Wallet id - Sheet.csv')  # The CSV you downloaded
    all_data = {}

    for wallet in wallets['wallet_id']:
        print(f"Fetching: {wallet}")
        txs = get_transactions(wallet)
        all_data[wallet] = txs

    with open('user_transactions.json', 'w') as f:
        json.dump(all_data, f, indent=2)

if __name__ == '__main__':
    main()


import json

with open("user_transactions.json", "r") as f:
    data = json.load(f)

print(list(data.keys())[:2])  # See first 2 wallet IDs
print(data[list(data.keys())[0]][0])  # Print first transaction of the first wallet
