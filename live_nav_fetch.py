import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw/nav_data", exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = f"data/raw/nav_data/{fund_name}.csv"

        nav_df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:
        print(f"Failed for {fund_name}")