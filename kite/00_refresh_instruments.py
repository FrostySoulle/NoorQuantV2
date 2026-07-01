#==========================================================
# Part 1 Imports
#==========================================================

from kiteconnect import KiteConnect
import pandas as pd
import json
import os

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

#==========================================================
# Part 2 Load Config
#==========================================================

with open("config.json", "r") as f:
    config = json.load(f)

kite = KiteConnect(api_key=config["api_key"])
kite.set_access_token(config["access_token"])

print("Connected to Kite")

#==========================================================
# Part 3 Download Instrument List
#==========================================================

print("Downloading NSE Instrument List...")

instruments = kite.instruments("NSE")

print("Downloaded", len(instruments), "instruments")

#==========================================================
# Part 4 Save CSV
#==========================================================

os.makedirs("data", exist_ok=True)

df = pd.DataFrame(instruments)

df = df[
    [
        "tradingsymbol",
        "instrument_token",
        "exchange"
    ]
]

filename = "data/instruments_nse.csv"

df.to_csv(
    filename,
    index=False
)

print("Saved:", filename)