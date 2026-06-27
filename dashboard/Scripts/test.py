import yfinance as yf
import pandas as pd

print("Downloading 15 minute data...")

df = yf.download(
    "ASIANPAINT.NS",
    period="30d",
    interval="15m",
    auto_adjust=True,
    progress=False
)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

print()
print("========================================")
print("ROWS")
print("========================================")
print(len(df))

print()
print("========================================")
print("FIRST 5 ROWS")
print("========================================")
print(df.head())

print()
print("========================================")
print("LAST 5 ROWS")
print("========================================")
print(df.tail())

print()
print("========================================")
print("COLUMNS")
print("========================================")
print(df.columns.tolist())

print()
print("========================================")
print("DATE RANGE")
print("========================================")

if not df.empty:
    print("Start:", df.index.min())
    print("End  :", df.index.max())
else:
    print("No data received")