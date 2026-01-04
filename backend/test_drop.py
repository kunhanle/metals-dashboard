import yfinance as yf
import pandas as pd

ticker = 'GC=F'
df = yf.download(ticker, period="5d", progress=False)

print(f"Original Columns: {df.columns}")
if isinstance(df.columns, pd.MultiIndex):
    print("Dropping level 1...")
    df.columns = df.columns.droplevel(1)
    print(f"New Columns: {df.columns}")
    print(f"Close: {df['Close'].iloc[0]}")
else:
    print("Single Index, no drop needed.")
