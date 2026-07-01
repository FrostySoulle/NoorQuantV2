#==========================================================
#Part 1 Imports
#==========================================================
import pandas as pd
import sys

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
#==========================================================
#Part 2 Load Dataset
#==========================================================
SAVE_RANKINGS = False
SAVE_RESEARCH = False

if len(sys.argv) < 3:
    print("Usage:")
    print("python 03_factor_research.py 60 RS_60 RVOL>1.5")
    exit()

DAYS = int(sys.argv[1])

if DAYS <= 60:
    MIN_TRADES = 20
elif DAYS <= 180:
    MIN_TRADES = 30
elif DAYS <= 365:
    MIN_TRADES = 50
else:
    MIN_TRADES = 100 
VALID_DATASETS = {60, 120, 180, 365, 730}

if DAYS not in VALID_DATASETS:
    print("Invalid dataset.")
    print("Choose: 60, 120, 180, 365, 730")
    exit()

MASTER_DATASET = (
    f"data/processed/{DAYS}d_master_dataset.csv"
)

print(f"Using dataset: {MASTER_DATASET}")

master_df = pd.read_csv(
    MASTER_DATASET,
    parse_dates=["Datetime"]
)

#==========================================================
#Part 3 Select Factor
#==========================================================

FACTOR_COLUMN = sys.argv[2]

print()
print("====================================")
print("Research Factor:", FACTOR_COLUMN)
print("====================================")
#==========================================================
#Part 4 Rank Factor
#==========================================================

research_df = master_df.copy()

FILTERS = sys.argv[3:]

for f in FILTERS:

    if ">" in f:
        column, value = f.split(">")
        research_df = research_df[
            research_df[column] > float(value)
        ]

    elif "<" in f:
        column, value = f.split("<")
        research_df = research_df[
            research_df[column] < float(value)
        ]
    print(f"{f:<20} -> {len(research_df)} rows")
    if research_df.empty:
      print("No rows remaining after filters.")
      exit()
        
research_df["Rank"] = (
    research_df
    .groupby("Datetime")[FACTOR_COLUMN]
    .rank(
        method="first",
        ascending=False
    )
    .astype(int)
)

#==========================================================
#Part 5 Save Research Dataset
#==========================================================
if SAVE_RESEARCH:
  research_df.to_csv(
      f"{DAYS}d_{FACTOR_COLUMN.lower()}_{'_'.join(FILTERS).replace('>','gt').replace('<','lt')}_research.csv",
      index=False
  )

#==========================================================
#Part 6 Rank Analysis 15m
#==========================================================

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
        ),
        Avg_Win=(
            "Future_15m",
            lambda x:x[x>0].mean()
        ),
        Avg_Loss=(
            "Future_15m",
            lambda x:x[x<0].mean()
        )
    )
)

rank_15m["Expectancy"] = (
    (rank_15m["Win_Rate"]/100)*rank_15m["Avg_Win"]
    +
    ((100-rank_15m["Win_Rate"])/100)*rank_15m["Avg_Loss"]
)
rank_15m=rank_15m.fillna(0)

if SAVE_RANKINGS:
    (
        rank_15m
        .sort_values(
            "Expectancy",
            ascending=False
        )
        .to_csv(
            f"{DAYS}d_{FACTOR_COLUMN.lower()}_rank_15m.csv",
            index=False
        )
    )

#==========================================================
#Part 7 Rank Analysis 30m
#==========================================================

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
        ),
        Avg_Win=(
            "Future_30m",
            lambda x:x[x>0].mean()
        ),
        Avg_Loss=(
            "Future_30m",
            lambda x:x[x<0].mean()
        )
    )
)

rank_30m["Expectancy"] = (
    (rank_30m["Win_Rate"]/100)*rank_30m["Avg_Win"]
    +
    ((100-rank_30m["Win_Rate"])/100)*rank_30m["Avg_Loss"]
)
rank_30m=rank_30m.fillna(0)

if SAVE_RANKINGS:
    (
        rank_30m
        .sort_values(
            "Expectancy",
            ascending=False
        )
        .to_csv(
            f"{DAYS}d_{FACTOR_COLUMN.lower()}_rank_30m.csv",
            index=False
        )
    )

#==========================================================
#Part 8 Rank Analysis 60m
#==========================================================

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
        ),
        Avg_Win=(
            "Future_60m",
            lambda x:x[x>0].mean()
        ),
        Avg_Loss=(
            "Future_60m",
            lambda x:x[x<0].mean()
        )
    )
)

rank_60m["Expectancy"] = (
    (rank_60m["Win_Rate"]/100)*rank_60m["Avg_Win"]
    +
    ((100-rank_60m["Win_Rate"])/100)*rank_60m["Avg_Loss"]
)
rank_60m=rank_60m.fillna(0)

if SAVE_RANKINGS:
    (
        rank_60m
        .sort_values(
            "Expectancy",
            ascending=False
        )
        .to_csv(
            f"{DAYS}d_{FACTOR_COLUMN.lower()}_rank_60m.csv",
            index=False
        )
    )

#==========================================================
#Part 9 Summary
#==========================================================

print()

report = ""
report += "=" * 60 + "\n"
report += f"Dataset : {DAYS} Days\n"
report += f"Factor  : {FACTOR_COLUMN}\n"
report += f"Filters : {' '.join(FILTERS) if FILTERS else 'None'}\n"
report += f"Rows    : {len(research_df)}\n"
report += f"Dates   : {research_df['Datetime'].nunique()}\n"
report += f"Stocks  : {research_df['Symbol'].nunique()}\n"
report += "=" * 60 + "\n\n"

best_timeframe = ""
best_expectancy = -999

for name, table in [
    ("15 Min", rank_15m),
    ("30 Min", rank_30m),
    ("60 Min", rank_60m),
]:

    valid = table[table["Count"] >= MIN_TRADES]

    if valid.empty:
        report += f"{name}: No valid results\n\n"
        continue

    best_rank = valid["Expectancy"].idxmax()

    current_expectancy = table.loc[best_rank, "Expectancy"]
    
    if current_expectancy > best_expectancy:
        best_expectancy = current_expectancy
        best_timeframe = name
    
    report += f"{name}\n"
    report += f"  Best Rank   : {best_rank}\n"
    report += f"  Trades      : {int(table.loc[best_rank, 'Count'])}\n"
    coverage = (
      table.loc[best_rank, "Count"]
      / len(research_df)
    ) * 100

    report += f"  Coverage    : {coverage:.2f}%\n"
    report += f"  Win Rate    : {table.loc[best_rank, 'Win_Rate']:.2f}%\n"
    report += f"  Avg Return  : {table.loc[best_rank, 'Avg_Return']:.3f}\n"
    report += f"  Expectancy  : {table.loc[best_rank, 'Expectancy']:.3f}\n"
    report += "-" * 40 + "\n"

report += f"Winner      : {best_timeframe}\n"
report += f"Best Edge   : {best_expectancy:.3f}\n"
report += "=" * 60 + "\n"

print(report)

RESULT = {
    "Dataset": DAYS,
    "Factor": FACTOR_COLUMN,
    "Filters": " ".join(FILTERS),
    "Rows": len(research_df),
    "Dates": research_df["Datetime"].nunique(),
    "Stocks": research_df["Symbol"].nunique(),
    "Winner": best_timeframe,
    "BestEdge": best_expectancy,
}
if __name__ != "__main__":
    pass

filename = "research_log.md"

with open(filename, "a") as f:
    f.write("\n\n")
    f.write("=" * 70)
    f.write("\n")
    f.write(report)
    
print(
f"RESULT|{DAYS}|{FACTOR_COLUMN}|{best_timeframe}|{best_expectancy}"
)
