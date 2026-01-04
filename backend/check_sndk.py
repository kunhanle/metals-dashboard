import yfinance as yf

tickers = ['SNDK', '8299.TWO', 'WDC']

for t in tickers:
    print(f"\nChecking {t}...")
    try:
        data = yf.download(t, period="1mo", progress=False)
        if data.empty:
            print(f"  {t}: NO DATA (Empty DataFrame)")
        else:
            print(f"  {t}: OK - {len(data)} rows")
            print(data.head(2))
    except Exception as e:
        print(f"  {t}: ERROR - {e}")
