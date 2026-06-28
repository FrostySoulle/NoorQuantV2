#==========================================================
#Part 1 Imports 
#==========================================================
import yfinance as yf
import pandas as pd 
import time 
import json
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


#==========================================================
#Part 2 Stocks 
#==========================================================

UNIVERSE_FILE = "../data/halal_universe.json"

print("Loading Halal Universe...")

with open(UNIVERSE_FILE, "r") as f:
    universe = json.load(f)

stocks = []

for stock in universe:
    stocks.append(stock["symbol"] + ".NS")

print("Loaded", len(stocks), "stocks")

#==========================================================
#Part 5 Loop stocks
#==========================================================
for symbol in stocks:

    print()
    print("Processing", symbol)

    time.sleep(1)

    df = pd.DataFrame()

    for attempt in range(3):

        print(f"Attempt {attempt+1}/3")

        df = yf.download(
            symbol,
            period="60d",
            interval="15m",
            auto_adjust=True,
            progress=False
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if not df.empty:
            print("Download Success")
            break

        print("Retrying...")
        time.sleep(3)

    if df.empty:
        print(f"FAILED AFTER 3 ATTEMPTS: {symbol}")
        continue

    print("Rows:", len(df))

#==========================================================
#Part 6 Save Raw Data
#==========================================================

    filename = symbol.replace(".NS", "") + ".csv"

    df.to_csv(
        "../data/raw/" + filename,
        index=True
    )

    print("Saved:", filename)
    print()
    print("======================================")
    print("DOWNLOAD COMPLETE")
    print("======================================")
    print(f"Downloaded {len(stocks)} symbols.")
