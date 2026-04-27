import pandas as pd

url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL"

df = pd.read_csv(url)

df.columns = ["Date", "Inflation"]
df["Date"] = pd.to_datetime(df["Date"])

df.to_csv("/Users/mohammadabdulmuneermognishaik/Documents/Projects/stock-market-data-pipeline/data/raw/inflation.csv", index=False)

print(df.head())