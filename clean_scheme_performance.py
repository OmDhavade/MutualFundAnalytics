import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


# Return columns
return_columns = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

print("=== RETURN VALUE VALIDATION ===")

# Validate returns are numeric
for col in return_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

    invalid_count = df[col].isna().sum()

    print(f"{col}: {invalid_count} invalid values")


print("\n=== RETURN ANOMALY CHECK ===")

# Flag anomalies
for col in return_columns:

    anomalies = df[
        (df[col] < -100) |
        (df[col] > 100)
    ]

    print(
        f"{col}: {len(anomalies)} anomalies"
    )

    if len(anomalies) > 0:
        anomalies.to_csv(
            f"data/processed/{col}_anomalies.csv",
            index=False
        )


print("\n=== EXPENSE RATIO VALIDATION ===")

# Convert expense ratio to numeric
df['expense_ratio_pct'] = pd.to_numeric(
    df['expense_ratio_pct'],
    errors='coerce'
)

# Check range 0.1% - 2.5%
invalid_expense = df[
    (df['expense_ratio_pct'] < 0.1) |
    (df['expense_ratio_pct'] > 2.5)
]

print(
    "Invalid Expense Ratios:",
    len(invalid_expense)
)

if len(invalid_expense) > 0:
    invalid_expense.to_csv(
        "data/processed/invalid_expense_ratio.csv",
        index=False
    )


print("\n=== DUPLICATE CHECK ===")

print(
    "Duplicate Rows:",
    df.duplicated().sum()
)

df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaning Completed Successfully")
print("Final Rows:", len(df))