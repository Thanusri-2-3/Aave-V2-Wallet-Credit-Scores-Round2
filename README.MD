# Wallet Risk Scoring From Scratch

This project implements a risk scoring system for Ethereum wallets using transaction data from the Aave protocol (or general Etherscan). The process involves collecting wallet transaction data, engineering useful features, and assigning a credit risk score from 0 to 1000 using unsupervised learning techniques.

## 📂 Project Files

- `wallets.csv`  
  Contains the list of 100 wallet addresses exported from the provided Google Sheet.

- `user_transactions.json`  
  JSON file storing raw transaction data for each wallet (fetched via Etherscan API).

- `wallet_features.csv`  
  Feature-engineered data including:
  - `num_transactions`: Total transactions per wallet
  - `total_eth_transferred`: Total ETH moved (in ETH)
  - `last_active_date`: Last transaction date
  - `total_gas_used`: Total gas used
  - `failed_transactions`: Count of failed txs

- `wallet_risk_scores.csv`  
  Final output with a credit risk score (0–1000) for each wallet based on scaled features.

## ⚙️ Workflow Steps

1. **Export Wallet Addresses**
   - Copied from Google Sheet → Saved to `wallets.csv`

2. **Fetch Transactions**
   - Used `fetch_transactions.py` to pull each wallet's data using the Etherscan API
   - Output saved in `user_transactions.json`

3. **Feature Engineering**
   - Ran `wallet_features.py` to compute meaningful transaction-based metrics
   - Output saved in `wallet_features.csv`

4. **Assign Risk Scores**
   - Ran `assign_risk_scores.py` to normalize data and compute a risk score
   - Used MinMaxScaler on key metrics like ETH value, gas used, and tx count
   - Final scores saved in `wallet_risk_scores.csv`

## 📌 Tech Stack

- Python 3.10+
- Libraries: `requests`, `pandas`, `scikit-learn`, `datetime`
- API Used: [Etherscan API](https://etherscan.io/apis)

## ✅ Result

Each wallet is assigned a risk score (0-1000), where:
- **0 = lowest activity/risk**
- **1000 = highest transaction volume, ETH transfer, gas usage, etc.**

This score can be used for initial creditworthiness analysis or DeFi risk prediction tasks.

---

**Prepared by:** Thanu Sri Reddy  
**Assignment:** Wallet Risk Scoring - Round 2  
**Date:** July 2025  
EOF
