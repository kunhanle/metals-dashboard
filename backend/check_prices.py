import yfinance as yf
import pandas as pd

METAL_TICKERS = {
    'Gold': 'GC=F',
    'Silver': 'SI=F',
    'Copper': 'HG=F',
    'Platinum': 'PL=F',
    'Palladium': 'PA=F',
    'Aluminium': 'ALI=F',
    'Nickel': 'NICK.L',
    'Zinc': 'ZNC=F',
}

print(f"{'Metal':<12} | {'Ticker':<10} | {'Rows':<5} | {'Latest':<10} | {'Mean':<10} | {'Status'}")
print("-" * 70)

for metal, ticker in METAL_TICKERS.items():
    try:
        df = yf.download(ticker, period="1mo", progress=False)
        
        if df.empty:
            print(f"{metal:<12} | {ticker:<10} | {'0':<5} | {'N/A':<10} | {'N/A':<10} | EMPTY")
            continue

        # Handle MultiIndex if present
        if isinstance(df.columns, pd.MultiIndex):
            close = df['Close'].iloc[:, 0]
        else:
            close = df['Close']
            
        latest = close.iloc[-1]
        mean_val = close.mean()
        is_zero = (close == 0).all()
        
        status = "OK"
        if is_zero or mean_val == 0:
            status = "ALL ZEROS"
        elif pd.isna(mean_val):
            status = "ALL NANS"
            
        print(f"{metal:<12} | {ticker:<10} | {len(df):<5} | {latest:<10.2f} | {mean_val:<10.2f} | {status}")

    except Exception as e:
        print(f"{metal:<12} | {ticker:<10} | ERROR: {e}")
