import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load wallet features
df = pd.read_csv("wallet_features.csv")

# Fill any missing values (e.g., if some wallets had no transactions)
df.fillna(0, inplace=True)

# Select numeric features for scoring
features = ['num_transactions', 'total_eth_transferred', 'total_gas_used']
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[features])

# Convert to risk scores: 0 (low risk) to 1000 (high risk)
risk_scores = (df_scaled.mean(axis=1) * 1000).astype(int)
df['risk_score'] = risk_scores

# Save the final results
df.to_csv("wallet_risk_scores.csv", index=False)
print("✅ wallet_risk_scores.csv has been created.")
