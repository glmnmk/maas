import yfinance as yf

ticker = "AAPL"
try:
    info = yf.Ticker(ticker).info
    print("KEYS:", info.keys())
    print("Country:", info.get("country"))
    print("Sector:", info.get("sector"))
except Exception as e:
    print("ERROR:", e)
