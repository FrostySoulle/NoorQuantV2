#==========================================================
#Part 1 Imports 
#==========================================================
from kiteconnect import KiteConnect
import pandas as pd 
import time 
import subprocess
import json
from datetime import datetime, timedelta

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
DOWNLOAD_DAYS = 730

#==========================================================
# Part 2 Stocks
#==========================================================

import subprocess

UNIVERSE_FILE = "halal_universe.json"

print("Loading Halal Universe...")

with open(UNIVERSE_FILE, "r") as f:
    universe = json.load(f)

print("Loaded", len(universe), "stocks")

#----------------------------------------------------------
# Ensure every stock has an instrument token
#----------------------------------------------------------

for stock in universe:

    if "instrument_token" not in stock:

        print(f"Updating {stock['symbol']}...")

        subprocess.run(
        [
            "python",
            "03_update_universe.py",
            stock["symbol"]
        ],
        check=True
    )

        with open(UNIVERSE_FILE, "r") as f:
            universe = json.load(f)

print("Universe Ready")
#==========================================================
# Part 3 Connect to Kite
#==========================================================

with open("config.json", "r") as f:
    config = json.load(f)

kite = KiteConnect(api_key=config["api_key"])
kite.set_access_token(config["access_token"])

print("Connected to Kite")
#==========================================================
# Part 4 Historical Data
#==========================================================
for stock in universe:

    symbol = stock["symbol"]
    instrument_token = stock["instrument_token"]

    print()
    print(f"Downloading {symbol}")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=DOWNLOAD_DAYS)
    
    all_candles = []
    
    while start_date < end_date:
    
        chunk_end = min(
            start_date + timedelta(days=200),
            end_date
        )
    
        print(
            f"Downloading "
            f"{start_date.date()} -> {chunk_end.date()}"
        )
    
        t1 = time.time()
    
        candles = kite.historical_data(
            instrument_token,
            start_date,
            chunk_end,
            "15minute"
        )
    
        t2 = time.time()
    
        print(
            f"Rows: {len(candles)} | "
            f"{t2-t1:.2f} sec"
        )
    
        all_candles.extend(candles)
    
        start_date = chunk_end + timedelta(days=1)
    
    df = pd.DataFrame(all_candles)
    
    df.rename(
    columns={
        "date": "Datetime",
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close",
        "volume": "Volume"
    },
    inplace=True
    )
    
    filename = f"data/raw/{symbol}.csv"
    
    df.to_csv(
        filename,
        index=False
    )
    
    print()
    print("Total Rows:", len(df))
    print("Saved:", filename)