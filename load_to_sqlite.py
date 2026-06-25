import pandas as pd
from sqlalchemy import create_engine

# Create SQLite connection
engine = create_engine(
    "sqlite:///mutualfund_analytics.db"
)

# Files to load
files = {
    "nav_history":
        "data/processed/nav_history_cleaned.csv",

    "investor_transactions":
        "data/processed/investor_transactions_cleaned.csv",

    "scheme_performance":
        "data/processed/scheme_performance_cleaned.csv"
}

# Load each CSV into SQLite
for table_name, file_path in files.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    csv_rows = len(df)

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{csv_rows} rows loaded into {table_name}"
    )

print("\nAll tables loaded successfully!")
