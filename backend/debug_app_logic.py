import yfinance as yf
import pandas as pd
import datetime

tickers = {'Gold': 'GC=F', 'CRU': 'HRC=F'}

end = datetime.datetime.now()
start = end - datetime.timedelta(days=1095)

print(f"Pandas version: {pd.__version__}")
print(f"Yfinance version: {yf.__version__}")

for name, ticker in tickers.items():
    print(f"\n--- {name} ({ticker}) ---")
    try:
        df = yf.download(ticker, start=start, end=end, interval="1d", progress=False)
        print(f"Columns type: {type(df.columns)}")
        print(f"Columns: {df.columns}")
        
        if isinstance(df.columns, pd.MultiIndex):
            print("Is MultiIndex")
            try:
                present_tickers = df.columns.get_level_values(1).unique()
                print(f"Present tickers in level 1: {present_tickers}")
                if len(present_tickers) > 0:
                    actual_ticker = present_tickers[0]
                    print(f"Extracting: {actual_ticker}")
                    df = df.xs(actual_ticker, axis=1, level=1)
                    print("Extraction success")
                    print(f"New Columns: {df.columns}")
            except Exception as e:
                print(f"Extraction Error: {e}")
        else:
            print("Is Single Index")

        # Check access
        if 'Close' in df.columns:
            print(f"First Close: {df['Close'].iloc[0]}")
        else:
            print("Missing Close column")

    except Exception as e:
        print(f"Download Error: {e}")
