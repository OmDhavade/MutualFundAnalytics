import sqlite3

# Create database file
conn = sqlite3.connect("mutualfund_analytics.db")

cursor = conn.cursor()

# Read SQL script
with open("sql/star_schema.sql", "r") as file:
    sql_script = file.read()

# Execute SQL
cursor.executescript(sql_script)

conn.commit()
conn.close()

print("Database and tables created successfully!")