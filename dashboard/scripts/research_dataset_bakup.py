import json 
import pandas as pd 
import yfinance as yf 
from datetime import datetime
import time

#FILE PATHS
UNIVERSE_FILE="../data/halal_universe.json"
OUTPUT_FILE="../data/research_data.csv"

#LOAD HALAL UNIVERSE
print("Loading halal universe....")
with open(UNIVERSE_FILE, "r") as f:
  universe = json.load(f)
  
print(f"Loaded {len(universe)}stocks")

#Download Nifty Data 
print("Downloading Nifty Data...")

nifty = yf.download(
  "^NSEI",
  period="1y",
  interval="1d",
  auto_adjust=True,
  progress=False
)

if isinstance(nifty.columns, pd.MultiIndex):
      nifty.columns=nifty.columns.get_level_values(0)
      
if nifty.empty:
  raise Exception("Failed to download NIFTY data")
  
print(f"NIFTY rows:{len(nifty)}")

#Create Research Dataset
dataset=[]
failed_stocks=[]

#Loop through every stock 
for stock in universe:
  symbol = stock["symbol"]
  yahoo_symbol = symbol + ".NS"
  print(f"Processing {symbol}")
  time.sleep(1)
  
  try:
    df = pd.DataFrame()

    for attempt in range(3):
    
        print(f"Attempt {attempt+1}/3")
    
        df = yf.download(
            yahoo_symbol,
            period="1y",
            interval="1d",
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
        failed_stocks.append(symbol)
        continue
    
#Match Stock Date With NIFTY Date
    common_dates = df.index.intersection(nifty.index)
    
    for i in range(len(common_dates)-5):
    
      date = common_dates[i]
      next_date = common_dates[i+1]
      future_date_5d = common_dates[i+5]
      stock_open = float(df.loc[date, "Open"])
      stock_close = float(df.loc[date, "Close"])
      nifty_open = float(nifty.loc[date, "Open"])
      nifty_close = float(nifty.loc[date, "Close"])
      
      #Returns
      stock_return = ((stock_close - stock_open) / stock_open)*100
      nifty_return = ((nifty_close - nifty_open) / nifty_open)*100
      
      #Relative_Strength
      rs_open = stock_return - nifty_return
      current_close = float(df.loc[date,"Close"])
      next_close = float(df.loc[next_date, "Close"])
      future_close_5d = float(df.loc[future_date_5d, "Close"])
      
      future_return_1d = (
        (next_close - current_close) / current_close 
        ) * 100
        
      future_return_5d = (
        (future_close_5d - current_close) / current_close 
        ) * 100
      
      #save_row
      dataset.append({
        "Date":date.strftime("%Y-%m-%d"),
        "Symbol":symbol,
        "Open":round(stock_open,2),
        "Close":round(stock_close,2),
        "Nifty_Open":round(nifty_open,2),
        "Nifty_Close":round(nifty_close,2),
        "Stocks_Return":round(stock_return,4),
        "Nifty_Return":round(nifty_return,4),
        "RS_Open":round(rs_open,4),
        "future_return_1d":round(future_return_1d,4),
        "future_return_5d":round(future_return_5d,4)
        })
    
  except Exception as e:
    print(f"Error processing {symbol}")
    print(e)
  
#save CSV
print("Creating DataFrame")

research_df = pd.DataFrame(dataset)

print("Calculating Ranks.....")
research_df["Rank"] = (
  research_df
  .groupby("Date")["RS_Open"]
  .rank(
    method="dense",
    ascending=False
    )
    .astype(int)
  )

research_df.to_csv(
  OUTPUT_FILE,
  index=False
  )

print()
print("RANK ANALYSIS")
print("========================================")

rank_summary = (
    research_df
    .groupby("Rank")
    .agg(
        Count=("future_return_5d","count"),
        Avg_Return=("future_return_5d","mean"),
        Median_Return=("future_return_5d","median"),
        Win_Rate=("future_return_5d",
                  lambda x: (x > 0).mean() * 100)
    )
)

rank_summary = rank_summary.round(2)

print(rank_summary)

rank_summary.to_csv(
    "../data/rank_analysis.csv"
)

print()
print("Saved:")
print("../data/rank_analysis.csv")
  
print()
print("========================================")
print("DATASET CREATED")
print("========================================")
print(f"Rows:{len(research_df)}")
print(f"File:{OUTPUT_FILE}")
print()
print("FAILED STOCKS")
print("========================================")
print(failed_stocks)