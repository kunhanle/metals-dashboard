import yfinance as yf
import pandas as pd
import datetime

STEEL_TICKERS = {
    'CRU Index': 'HRC=F',
    'DJUSST': '^DJUSST',
    'HRC Futures': 'HRC=F',
    'SGX Iron Ore': 'TIO=F',
}

end = datetime.datetime.now()
start = end - datetime.timedelta(days=1095) # 3 years

print(f"Fetching from {start.date()} to {end.date()}")

for name, ticker in STEEL_TICKERS.items():
    print(f"\n--- {name} ({ticker}) ---")
    try:
        df = yf.download(ticker, start=start, end=end, interval="1d", progress=False)
        
        if df.empty:
            print("EMPTY DATAFRAME")
            continue
            
        print(f"Columns: {df.columns}")
        print(f"Rows: {len(df)}")
        
        # Mimic app.py processing
        if isinstance(df.columns, pd.MultiIndex):
            try:
                # app.py logic: df = df.xs(ticker, axis=1, level=1)
                # But sometimes level 1 isn't ticker if single symbol download?
                # or if it is single level.
                print("MultiIndex detected.")
                print(df.head(2))
            except Exception as e:
                print(f"MultiIndex Error: {e}")
                
        # Check actual values
        if 'Close' in df.columns: # Simple check
             print(f"First Close: {df['Close'].iloc[0]}")
             print(f"Last Close: {df['Close'].iloc[-1]}")
        else:
             print("Close column missing?")

    except Exception as e:
        print(f"ERROR: {e}")
