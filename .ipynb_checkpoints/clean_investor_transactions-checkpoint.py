import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

# Fix date format
df['transaction_date'] = pd.to_datetime(
    df['transaction_date'],
    errors='coerce'
)

# Standardize transaction type
mapping = {
    'Sip': 'SIP',
    'Lumpsum': 'Lumpsum',
    'Redemption': 'Redemption'
}

df['transaction_type'] = (
    df['transaction_type']
    .astype(str)
    .str.strip()
    .str.title()
    .replace(mapping)
)

# Validate amount
invalid_amount = df[df['amount_inr'] <= 0]

print("Invalid Amount Rows:", len(invalid_amount))

df = df[df['amount_inr'] > 0]

# Clean KYC status
df['kyc_status'] = (
    df['kyc_status']
    .astype(str)
    .str.strip()
    .str.title()
)

# Check invalid KYC values
valid_kyc = ['Verified', 'Pending', 'Rejected']

invalid_kyc = df[
    ~df['kyc_status'].isin(valid_kyc)
]

print("Invalid KYC Records:", len(invalid_kyc))

# Remove duplicates
print("Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

# Save
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Cleaning Completed Successfully")
print("Final Rows:", len(df))