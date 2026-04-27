import pandas as pd
import sqlite3
import os

# -------------------------
# CONNECT TO DATABASE
# -------------------------
conn = sqlite3.connect("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/database/stock.db")

# -------------------------
# LOAD CSV FILES
# -------------------------

# INTEREST RATES
rates = pd.read_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/FEDFUNDS_2Y.csv")
rates.to_sql("interest_rates", conn, if_exists="replace", index=False)

# INFLATION
inflation = pd.read_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/inflation.csv")
inflation.to_sql("inflation", conn, if_exists="replace", index=False)

# VIX
vix = pd.read_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/VIX.csv")
vix.to_sql("vix", conn, if_exists="replace", index=False)

# QQQ
qqq = pd.read_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/QQQ.csv")
qqq.to_sql("qqq", conn, if_exists="replace", index=False)

# Oil
oil = pd.read_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/CL=F_oil.csv")
oil.to_sql("oil", conn, if_exists="replace", index=False)

# Gas
Gas = pd.read_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/NG=F_gas.csv")
Gas.to_sql("Gas", conn, if_exists="replace", index=False)

# -------------------------
# CLOSE CONNECTION
# -------------------------
conn.close()

print("All datasets loaded into stocks.db successfully")