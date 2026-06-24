import json 
import pandas as pd 
import yfinance as yf 
from datetime import datetime

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

#Loop through every stock 
for stock in universe:
  symbol = stock["symbol"]
  yahoo_symbol = symbol + ".NS"
  print(f"Processing {symbol}")
  
  try:
    df = yf.download(
      yahoo_symbol,
      period = "1y",
      interval="1d",
      auto_adjust=True,
      progress=False
    )
    
    if isinstance(df.columns, pd.MultiIndex):
      df.columns=df.columns.get_level_values(0)
    
    if df.empty:
      print(f"Skipping {symbol} (no data")
      continue
    
#Match Stock Date With NIFTY Date
    common_dates = df.index.intersection(nifty.index)
    
    for date in common_dates:
      stock_open = float(df.loc[date, "Open"])
      stock_close = float(df.loc[date, "Close"])
      nifty_open = float(nifty.loc[date, "Open"])
      nifty_close = float(nifty.loc[date, "Close"])
      
    #Returns
    stock_return = ((stock_close - stock_open) / stock_open)*100
    nifty_return = ((nifty_close - nifty_open) / nifty_open)*100
    
    #Relative_Strength
    rs_open = stock_return - nifty_return
    
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
      "RS_Open":round(rs_open,4)
      })
    
  except Exception as e:
    print(f"Error processing {symbol}")
    print(e)
  
#save CSV
print("Creating DataFrame")

research_df = pd.DataFrame(dataset)

research_df.to_csv(
  OUTPUT_FILE,
  index=False
  )
  
print()
print("========================================")
print("DATASET CREATED")
print("========================================")
print(f"Rows:{len(research_df)}")
print(f"File:{OUTPUT_FILE}")
print("========================================")
