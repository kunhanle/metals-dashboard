import yfinance as yf

# Candidates
tickers = [
    '^DJUSST', # Dow Jones Iron & Steel
    'HRC=F',   # US Midwest Domestic Hot-Rolled Coil Steel (futures often settle to CRU)
    'HR=F',    # Alternative for HRC
    'TIO=F',   # SGX Iron Ore (62% Fe)
    'SCO=F',   # Dalian Iron Ore? Or something else. (Actually TIO is often SGX)
    'FEF=F',   # Search suggested this
    'MT',      # ArcelorMittal (Steel proxy?) - User asked for Index though.
    'X'        # US Steel
]

print(f"{'Ticker':<10} | {'Rows':<5} | {'Latest':<10} | Status")
print("-" * 50)

try:
    data = yf.download(tickers, period="1mo", progress=False, group_by='ticker')
    
    for t in tickers:
        try:
            if len(tickers) > 1:
                df = data[t]
            else:
                df = data
                
            if df.empty:
                print(f"{t:<10} | 0     | N/A        | EMPTY")
                continue
            
            # Check for multiple columns if multi-index not fully handled by group_by 
            # (group_by='ticker' usually handles it well)
            close = df['Close']
            
            # If all NaNs
            if close.isna().all():
                 print(f"{t:<10} | 0     | N/A        | EMPTY COLS")
                 continue

            latest = close.dropna().iloc[-1] if not close.dropna().empty else float('nan')
            count = len(close.dropna())
            print(f"{t:<10} | {count:<5} | {latest:<10.2f} | OK")
        except Exception as e:
            print(f"{t:<10} | ERROR | {str(e)[:15]} | ERROR")

except Exception as main_e:
    print(f"Main Error: {main_e}")
