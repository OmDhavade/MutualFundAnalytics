import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(
    by=['amfi_code', 'date']
)

df = df.drop_duplicates(
    subset=['amfi_code', 'date']
)

df = df[df['nav'] > 0]

all_funds = []

for code, group in df.groupby('amfi_code'):

    group = group.set_index('date')

    full_dates = pd.date_range(
        start=group.index.min(),
        end=group.index.max(),
        freq='D'
    )

    group = group.reindex(full_dates)

    group['amfi_code'] = code

    all_funds.append(group)

df = pd.concat(all_funds)

df['nav'] = df.groupby('amfi_code')['nav'].ffill()

df = df.reset_index()

df.rename(
    columns={'index': 'date'},
    inplace=True
)

assert (df['nav'] > 0).all()

# Save
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Cleaning Completed Successfully")

print("Total Records:", len(df))
print("Duplicate Rows:", df.duplicated().sum())
print("Missing NAV Values:", df['nav'].isnull().sum())
print("Minimum NAV:", df['nav'].min())
