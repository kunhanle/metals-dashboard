import yfinance as yf
import datetime

tickers = ['LEAD.L', 'PB=F', 'LME-PB', 'LEAD']

print(f"{'Ticker':<10} | {'Rows':<5} | {'Latest':<10} | Status")
print("-" * 50)

end = datetime.datetime.now()
start = end - datetime.timedelta(days=365) # 1 year

try:
    data = yf.download(tickers, start=start, end=end, interval="1d", progress=False, group_by='ticker')
    
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
