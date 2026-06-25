import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print(df.head())

#Check Dataset Size
print("Rows and Columns:")
print(df.shape)

# See All Column Names
print("\nColumns:")
print(df.columns.tolist())

# Check Data Types
print("\nData Types:")
print(df.dtypes)

# Count Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# unique Fund Houses
print("\nFund Houses:")
print(df["fund_house"].unique())
# nunique fund houses
print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

# Print unique Categories
print("\nCategories:")
print(df["category"].unique())

print("\nCategory Counts:")
print(df["category"].value_counts())

# Print unique Sub-Categories
print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nSub Category Counts:")
print(df["sub_category"].value_counts())

