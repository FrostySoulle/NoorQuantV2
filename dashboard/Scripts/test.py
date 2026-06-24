import yfinance as yf
df=yf.download(
  "ASIANPAINT.NS",
  period="5d",
  progress=False
  )
print(df.head())