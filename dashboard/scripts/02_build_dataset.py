#==========================================================
#Part 1 Imports 
#==========================================================
import pandas as pd 
import pandas_ta as ta
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
    
    cum_pv = 0
    cum_volume = 0
    last_date = None
     
    df["ATR"] = ta.atr(
        df["High"],
        df["Low"],
        df["Close"],
        length=14
    )
    
    df["EMA20"] = ta.ema(df["Close"],
    length=20)

    for i in range(2, len(common_dates) - 4):
  
        dt = common_dates[i]

        if pd.isna(df.loc[dt,"ATR"]):
            continue
        
        if pd.isna(df.loc[dt,"EMA20"]):
            continue
        
        today = dt.date()
  
        if df.loc[dt,"Time"] != "09:15":
            continue
        
        if today != last_date:
            cum_pv = 0
            cum_volume = 0
            last_date = today
            
        previous_close = float(df.loc[common_dates[i-1], "Close"])
        
        previous_previous_close = float(df.loc[common_dates[i-2],"Close"])
        
        previous_day_return = (
            (previous_close -
            previous_previous_close)
            / previous_previous_close
        )*100

        current_open = float(df.loc[dt, "Open"])
        current_close = float(df.loc[dt, "Close"])
        current_volume = float(df.loc[dt, "Volume"])

        close_15 = float(df.loc[common_dates[i-1], "Close"])
        close_30 = float(df.loc[common_dates[i-2], "Close"])
        close_60 = float(df.loc[common_dates[i-4], "Close"])

        RS_15 = (
    (current_close - close_15)
    / close_15
) * 100

        RS_30 = (
    (current_close - close_30)
    / close_30
) * 100

        RS_60 = (
    (current_close - close_60)
    / close_60
) * 100
        
        orb_high=float(df.loc[dt,"High"])
        orb_low=float(df.loc[dt,"Low"])
        orb_range=orb_high-orb_low
        orb_percent = (orb_high-orb_low)/ current_open*100
        orb_body = abs(current_close-
        current_open)/current_open*100
        
        gap = (
            (current_open - previous_close)
            / previous_close
        ) * 100
        
        past_volumes = []

        for j in range(i-26, i):
            if j >= 0 and df.iloc[j]["Time"] == "09:15":
                past_volumes.append(df.iloc[j]["Volume"])

        if len(past_volumes) == 0:
            continue

        average_volume = pd.Series(past_volumes).mean()

        rvol = current_volume / average_volume
        
        typical_price = (
            current_close +
            orb_high +
            orb_low
        ) /3
        
        cum_pv += typical_price * current_volume
        cum_volume += current_volume
        
        vwap = cum_pv / cum_volume
        
        VWAP_Distance = (
            (current_close - vwap)
            / vwap
        )*100
        
        ATR_Percent =(
            df.loc[dt,"ATR"]
            / current_close
        )*100
        
        EMA20_Distance =(
            (current_close - df.loc[dt,"EMA20"])
            /df.loc[dt,"EMA20"]
        )*100
            
        future15 = common_dates[i+1]
        future30 = common_dates[i+2]
        future60 = common_dates[i+4]

#==========================================================
#Part 7 Future Returns
#==========================================================

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
        "Previous_Day_Return":round(previous_day_return,4),
        "RVOL":round(rvol,4),
        
        "ORB_High":round(orb_high,4),
        "ORB_Low":round(orb_low,4),      
        "ORB_Range":round(orb_range,4),
        "ORB_Percent":round(orb_percent,4),
        "ORB_Body":round(orb_body,4),
        
        "VWAP_Distance":round(VWAP_Distance,4),
        "ATR_Percent":round(ATR_Percent,4),
        "EMA20_Distance":round(EMA20_Distance,4),
        
        "Future_15m":round(return15,4),
        "Future_30m":round(return30,4),
        "Future_60m":round(return60,4),
        "RS_15": round(RS_15,4),
        "RS_30": round(RS_30,4),
        "RS_60": round(RS_60,4),
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