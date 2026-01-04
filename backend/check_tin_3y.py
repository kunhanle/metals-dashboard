import yfinance as yf
import datetime

end = datetime.datetime.now()
start = end - datetime.timedelta(days=1095)

print(f"Fetching TIN.L from {start.date()} to {end.date()}")
try:
    df = yf.download('TIN.L', start=start, end=end, interval="1d", progress=False)
    print(f"Rows: {len(df)}")
    if not df.empty:
        print(f"First: {df.index[0]}")
        print(f"Last: {df.index[-1]}")
    else:
        print("EMPTY DATAFRAME")
except Exception as e:
    print(f"ERROR: {e}")
