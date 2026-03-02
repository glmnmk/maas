import yfinance as yf

for ticker in ["AAPL", "GOOG", "TLT"]:
    try:
        info = yf.Ticker(ticker).info
        print(f"--- {ticker} ---")
        print("Country:", info.get("country"))
        print("Sector:", info.get("sector"))
    except Exception as e:
        print(f"ERROR for {ticker}:", e)
