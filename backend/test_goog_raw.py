import asyncio
import pandas as pd
from app.market_data import get_wrds_connection
import os
from dotenv import load_dotenv

load_dotenv()

async def test():
    db = get_wrds_connection()
    if db:
        meta_sql = """
        SELECT a.tic, b.loc as country, b.gsector as sector
        FROM comp_na_daily_all.names a
        JOIN comp.company b ON a.gvkey = b.gvkey
        WHERE a.tic = 'GOOG'
        """
        df = db.raw_sql(meta_sql)
        print("GOOG RAW ROWS:", len(df))
        print(df)
        
        meta_sql_2 = """
        SELECT a.tic, b.loc as country, b.gsector as sector
        FROM comp_na_daily_all.names a
        JOIN comp.company b ON a.gvkey = b.gvkey
        WHERE a.tic = 'GOOGL'
        """
        df2 = db.raw_sql(meta_sql_2)
        print("GOOGL RAW ROWS:", len(df2))
        print(df2)

if __name__ == "__main__":
    asyncio.run(test())
