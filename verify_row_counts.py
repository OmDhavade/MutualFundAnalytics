import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///mutualfund_analytics.db"
)

files = {
    "nav_history":
        "data/processed/nav_history_cleaned.csv",

    "investor_transactions":
        "data/processed/investor_transactions_cleaned.csv",

    "scheme_performance":
        "data/processed/scheme_performance_cleaned.csv"
}

print("\nROW COUNT VALIDATION\n")

for table_name, file_path in files.items():

    csv_rows = len(
        pd.read_csv(file_path)
    )

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table_name}",
        engine
    )["cnt"][0]

    status = (
        "PASS"
        if csv_rows == db_rows
        else "FAIL"
    )

    print(
        f"{table_name}: "
        f"CSV={csv_rows}, "
        f"DB={db_rows}, "
        f"{status}"
    )