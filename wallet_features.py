import pandas as pd
import json
from datetime import datetime

# Load transaction data
with open("user_transactions.json", "r") as f:
    data = json.load(f)

# List to store per-wallet features
features = []

for wallet, txs in data.items():
    if not isinstance(txs, list) or not txs:
        continue  # skip empty or invalid entries

    # Total number of transactions
    num_tx = len(txs)

    # Total ETH transferred (convert from wei to ETH)
    total_eth = sum(int(tx["value"]) / 1e18 for tx in txs)

    # Last active time
    timestamps = [int(tx["timeStamp"]) for tx in txs if "timeStamp" in tx]
    last_active = datetime.utcfromtimestamp(max(timestamps)).strftime("%Y-%m-%d") if timestamps else None

    # Gas used
    total_gas = sum(int(tx.get("gasUsed", 0)) for tx in txs)

    # Failed transactions
    failed_tx = sum(1 for tx in txs if tx.get("isError", "0") == "1")

    features.append({
        "wallet": wallet,
        "num_transactions": num_tx,
        "total_eth_transferred": total_eth,
        "last_active_date": last_active,
        "total_gas_used": total_gas,
        "failed_transactions": failed_tx,
    })

# Save to CSV
df = pd.DataFrame(features)
df.to_csv("wallet_features.csv", index=False)
print("✅ wallet_features.csv has been created.")
