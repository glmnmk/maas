import asyncio
from app.market_data import get_asset_metadata
import os
from dotenv import load_dotenv

load_dotenv()

async def test():
    tickers = ["AAPL", "GOOG", "GOOGL", "MSFT", "AMZN"]
    for t in tickers:
        print(f"--- Testing {t} ---")
        meta = get_asset_metadata(t)
        print("Metadata:", meta)

if __name__ == "__main__":
    asyncio.run(test())
