import asyncio
from app.main import analyze_portfolio
from app.models import PortfolioRequest

async def run():
    req = PortfolioRequest(tickers=["AAPL", "MSFT", "AMZN", "GOOG"])
    try:
        res = await analyze_portfolio(req)
        # res is a dict here because we return a dict directly in analyze_portfolio function body
        if isinstance(res, dict):
            assets = res.get("individual_assets", [])
        else:
            assets = getattr(res, "individual_assets", [])
        for a in assets:
            if isinstance(a, dict):
                print(f"{a['ticker']}: {a.get('sector', 'None')} - {a.get('country', 'None')}")
            else:
                print(f"{a.ticker}: getattr sector failed")
    except Exception as e:
        print("ERROR", str(e))

asyncio.run(run())
