import sqlite3
import pandas as pd
conn = sqlite3.connect("database/stock.db")
df = pd.read_sql("SELECT * FROM stock_prices LIMIT 10;", conn)
print(df)
conn.close()