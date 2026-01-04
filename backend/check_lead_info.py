import yfinance as yf

ticker = yf.Ticker("LEAD")
print(f"Short Name: {ticker.info.get('shortName')}")
print(f"Long Name: {ticker.info.get('longName')}")
print(f"Symbol: {ticker.info.get('symbol')}")
print(f"Exchange: {ticker.info.get('exchange')}")
print(f"QuoteType: {ticker.info.get('quoteType')}")
