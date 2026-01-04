import yfinance as yf

tickers = ['8299.TWO', 'AAPL', '2330.TW']

for t in tickers:
    try:
        tick = yf.Ticker(t)
        info = tick.info
        print(f"--- {t} ---")
        print(f"Short Name: {info.get('shortName')}")
        print(f"Long Name: {info.get('longName')}")
    except Exception as e:
        print(f"Error {t}: {e}")
