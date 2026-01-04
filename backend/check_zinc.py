import yfinance as yf
import pandas as pd

candidates = ['ZNC=F', 'ZINC.L', 'LMZ=F']

for t in candidates:
    print(f"\nAnalyzing {t} (1y)...")
    try:
        df = yf.download(t, period="1y", progress=False)
        if df.empty:
            print("  EMPTY")
            continue
            
        if isinstance(df.columns, pd.MultiIndex):
            close = df['Close'].iloc[:, 0]
        else:
            close = df['Close']
            
        print(f"  Rows: {len(df)}")
        print(f"  Zeros: {(close == 0).sum()}")
        print(f"  NaNs: {close.isna().sum()}")
        print(f"  Mean: {close.mean()}")
        print(f"  Min: {close.min()}")
        print(f"  Max: {close.max()}")
        print("  Head 5:")
        print(close.head().to_string())
        print("  Tail 5:")
        print(close.tail().to_string())
        
    except Exception as e:
        print(f"  ERROR: {e}")
