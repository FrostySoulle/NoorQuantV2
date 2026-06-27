#==========================================================
#Part 1 Imports 
#==========================================================
import yfinance as yf
import pandas as pd 
import time 
import json

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
#Part 3 Download Nifty 
#==========================================================
print("Downloading NIFTY.....")

nifty = pd.DataFrame()

for attempt in range(3):

    print(f"NIFTY Attempt {attempt+1}/3")

    nifty = yf.download(
        "^NSEI",
        period="30d",
        interval="15m",
        auto_adjust=True,
        progress=False
    )

    if isinstance(nifty.columns, pd.MultiIndex):
        nifty.columns = nifty.columns.get_level_values(0)

    if not nifty.empty:
        print("NIFTY Success")
        break

    print("Retrying NIFTY...")
    time.sleep(3)

if nifty.empty:
    raise Exception("NIFTY download failed")

print("NIFTY Rows:", len(nifty))

#==========================================================
#Part 4 Dataset 
#==========================================================
dataset=[]

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
            period="30d",
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
#Part 6 Create RS Rows
#==========================================================

    common_dates = df.index.intersection(nifty.index)

    for i in range(len(common_dates) - 4):
  
        dt = common_dates[i]
  
        future15 = common_dates[i + 1]
        future30 = common_dates[i + 2]
        future60 = common_dates[i + 4]
  
        stock_open = float(df.loc[dt, "Open"])
        stock_close = float(df.loc[dt, "Close"])
  
        nifty_open = float(nifty.loc[dt, "Open"])
        nifty_close = float(nifty.loc[dt, "Close"])
  
        stock_return = (
            (stock_close - stock_open)
            / stock_open
        ) * 100
  
        nifty_return = (
            (nifty_close - nifty_open)
            / nifty_open
        ) * 100
  
        rs = stock_return - nifty_return
        
#==========================================================
#Part 7 Future Returns
#==========================================================

        current_close = float(df.loc[dt, "Close"])
  
        close15 = float(df.loc[future15, "Close"])
        close30 = float(df.loc[future30, "Close"])
        close60 = float(df.loc[future60, "Close"])
  
        return15 = (
            (close15 - current_close)
            / current_close
        ) * 100
  
        return30 = (
            (close30 - current_close)
            / current_close
        ) * 100
  
        return60 = (
            (close60 - current_close)
            / current_close
        ) * 100
        
#==========================================================
#Part 8 Save Row
#==========================================================
        dataset.append({
        "Datetime":dt,        
        "Symbol":symbol,
        "RS_Open":round(rs,4),
        "Future_15m":round(return15,4),
        "Future_30m":round(return30,4),
        "Future_60m":round(return60,4),
        })
#==========================================================
#Part 9 DataFrame
#==========================================================
research_df = pd.DataFrame(dataset)
print()
print("Rows:",len(research_df))
#==========================================================
#Part 10 Rank
#==========================================================
print(research_df.head())
print(len(research_df))
research_df["Rank"]=(
  research_df
  .groupby("Datetime")["RS_Open"]
  .rank(
    method="dense",
    ascending=False
  )
  .astype(int)
)
#==========================================================
#Part 11 Save CSV
#==========================================================
research_df.to_csv(
  "intraday_research.csv",
  index=False
  )
print()
print("Saved:")
print("intraday_research.csv")
#==========================================================
#Part 12 Rank Analysis 15m
#==========================================================
print()
print("15 Min Analysis")
print("====================================================")
rank_15m = (
  research_df
  .groupby("Rank")
  .agg(
    Count=("Future_15m","count"),
    Avg_Return=("Future_15m","mean"),
    
    Median_Return=("Future_15m","median"),
      Win_Rate=(
        "Future_15m",
        lambda x:(x>0).mean()*100
      )
    )
  )
print(rank_15m.round(2))

rank_15m.to_csv(
    "rank_15m.csv"
)
#==========================================================
#Part 13 30 Minute Analysis
#==========================================================
print()
print("30 Min Analysis")
print("====================================================")
rank_30m = (
  research_df
  .groupby("Rank")
  .agg(
    Count=("Future_30m","count"),
    Avg_Return=("Future_30m","mean"),
    
    Median_Return=("Future_30m","median"),
      Win_Rate=(
        "Future_30m",
        lambda x:(x>0).mean()*100
      )
    )
  )
print(rank_30m.round(2))

rank_30m.to_csv(
    "rank_30m.csv"
)
#==========================================================
#Part 14 60 Minute Analysis
#==========================================================
print()
print("60 Min Analysis")
print("====================================================")
rank_60m = (
  research_df
  .groupby("Rank")
  .agg(
    Count=("Future_60m","count"),
    Avg_Return=("Future_60m","mean"),
    
    Median_Return=("Future_60m","median"),
      Win_Rate=(
        "Future_60m",
        lambda x:(x>0).mean()*100
      )
    )
  )
print(rank_60m.round(2))

rank_60m.to_csv(
    "rank_60m.csv"
)