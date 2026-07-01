#==========================================================
# Part 1 Imports
#==========================================================

import pandas as pd
import json
import sys

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

#==========================================================
# Part 2 Inputs
#==========================================================

SYMBOL = sys.argv[1]

UNIVERSE_FILE = "halal_universe.json"
INSTRUMENT_FILE = "data/instruments_nse.csv"

#==========================================================
# Part 3 Load Files
#==========================================================

print("Loading Universe...")

with open(UNIVERSE_FILE, "r") as f:
    universe = json.load(f)

print("Loading Instrument List...")

instrument_df = pd.read_csv(INSTRUMENT_FILE)

#==========================================================
# Part 4 Find Instrument Token
#==========================================================

match = instrument_df[
    instrument_df["tradingsymbol"] == SYMBOL
]

if match.empty:
    raise Exception(f"{SYMBOL} not found in instrument list.")

instrument_token = int(
    match.iloc[0]["instrument_token"]
)

print(f"Found {SYMBOL} -> {instrument_token}")

#==========================================================
# Part 5 Update Universe
#==========================================================

updated = False

for stock in universe:

    if stock["symbol"] == SYMBOL:

        stock["instrument_token"] = instrument_token
        updated = True
        break

if not updated:
    raise Exception(f"{SYMBOL} not found in universe.")

#==========================================================
# Part 6 Save Universe
#==========================================================

with open(UNIVERSE_FILE, "w") as f:
    json.dump(universe, f, indent=2)

print(f"Updated {SYMBOL} successfully.")