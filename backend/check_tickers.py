import yfinance as yf

candidates = [
    'PHNI.L', # WisdomTree Nickel
    'HNM.L',  # Another potential
    'NICK.L'
]

for t in candidates:
    try:
        data = yf.download(t, period="5d", progress=False)
        if not data.empty:
            print(f"[PASS] {t} returned {len(data)} rows")
        else:
            print(f"[FAIL] {t} returned empty")
    except:
        print(f"[ERR] {t}")
