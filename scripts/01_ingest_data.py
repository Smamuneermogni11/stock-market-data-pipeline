import yfinance as yf
import pandas as pd
import os
ticker = "MSFT"
df = yf.download(ticker,period="2y")
os.makedirs("data/raw",exist_ok=True)
file_path = f"data/raw/{ticker}_stock.csv"
df.to_csv(file_path)
print("Saved to:", file_path)
