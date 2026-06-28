#==========================================================
#Part 1 Imports 
#==========================================================
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
#Part 4 Dataset 
#==========================================================
dataset=[]

#==========================================================
#Part 5 Loop stocks
#==========================================================
for symbol in stocks:

    print()
    print("Processing", symbol)

    filename = "../data/raw/" + symbol.replace(".NS","") + ".csv"

    df = pd.read_csv(
        filename,
        index_col=0,
        parse_dates=True
    )

    if df.empty:
        print("FAILED")
        continue

    print("Rows:", len(df))
    df["Time"]=df.index.strftime("%H:%M")
    
#==========================================================
#Part 6 Create Research Dataset
#==========================================================

    common_dates = df.index

    for i in range(1, len(common_dates) - 4):
  
        dt = common_dates[i]
  
        if df.loc[dt,"Time"] != "09:15":
            continue
  
        previous_close = float(df.loc[common_dates[i-1], "Close"])

        current_open = float(df.loc[dt, "Open"])

        gap = (
            (current_open - previous_close)
            / previous_close
        ) * 100
        
        future15 = common_dates[i+1]
        future30 = common_dates[i+2]
        future60 = common_dates[i+4]

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
        
        "Gap":round(gap,4),
        
        "Future_15m":round(return15,4),
        "Future_30m":round(return30,4),
        "Future_60m":round(return60,4),
        })
#==========================================================
#Part 9 DataFrame
#==========================================================
master_df = pd.DataFrame(dataset)
print()
print("Unique Stocks :", master_df["Symbol"].nunique())
print("Unique Dates  :", master_df["Datetime"].nunique())
print("Average Rows per Stock :", len(master_df)/master_df["Symbol"].nunique())
print("Rows:",len(master_df))
#==========================================================
#Part 10 Save Master Dataset
#==========================================================
master_df.to_csv(
    "../data/processed/master_dataset.csv",
    index=False
)
print()
print("Saved:")
print("../data/processed/master_dataset.csv")