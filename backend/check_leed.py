import yfinance as yf

tickers = ['LEED.L', 'LEED', 'AIGC.L'] 

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
                
            close = df['Close']
            if close.empty:
                 print(f"{t:<10} | 0     | N/A        | EMPTY COLS")
                 continue

            latest = close.dropna().iloc[-1] if not close.dropna().empty else float('nan')
            count = len(close.dropna())
            print(f"{t:<10} | {count:<5} | {latest:<10.2f} | OK")
        except Exception as e:
            print(f"{t:<10} | ERROR | {str(e)[:15]} | ERROR")
except Exception as main_e:
    print(f"Main Error: {main_e}")
