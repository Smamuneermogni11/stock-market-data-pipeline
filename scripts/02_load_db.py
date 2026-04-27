import pandas as pd
import sqlite3
import os
df = pd.read_csv("data/raw/MSFT_stock.csv")
os.makedirs("database",exist_ok=True)
conn = sqlite3.connect("database/stock.db")
df.to_sql("stock_prices", conn, if_exists= "replace", index=False)
print("Data succefully loaded into SQlite database!")
conn.close()