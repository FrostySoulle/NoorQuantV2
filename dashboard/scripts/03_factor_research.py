#==========================================================
#Part 1 Imports
#==========================================================
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
#==========================================================
#Part 2 Load Dataset
#==========================================================

MASTER_DATASET = "../data/processed/master_dataset.csv"

master_df = pd.read_csv(
    MASTER_DATASET,
    parse_dates=["Datetime"]
)

print("Rows after filter:", len(master_df))
print("Stocks :", master_df["Symbol"].nunique())
print("Days :", master_df["Datetime"].dt.date.nunique())
#==========================================================
#Part 3 Select Factor
#==========================================================

FACTOR_COLUMN = "RS"

print()
print("====================================")
print("Research Factor:", FACTOR_COLUMN)
print("====================================")
#==========================================================
#Part 4 Rank Factor
#==========================================================

research_df = master_df.copy()

research_df =research_df[research_df["RVOL"]>1]

research_df["Rank"] = (
    research_df
    .groupby("Datetime")[FACTOR_COLUMN]
    .rank(
        method="first",
        ascending=False
    )
    .astype(int)
)

print()
print("Ranking Complete")
print(research_df.head())

print()
print("Rows After Filter:",len(research_df))
print()

#==========================================================
#Part 5 Save Research Dataset
#==========================================================

research_df.to_csv(
    f"{FACTOR_COLUMN.lower()}_research.csv",
    index=False
)

print("Saved:")
print(f"{FACTOR_COLUMN.lower()}_research.csv")

#==========================================================
#Part 6 Rank Analysis 15m
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
print(rank_15m.round(3))

rank_15m.to_csv(
    f"{FACTOR_COLUMN.lower()}_rank_15m.csv"
)

#==========================================================
#Part 7 Rank Analysis 30m
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
print(rank_30m.round(3))

rank_30m.to_csv(
    f"{FACTOR_COLUMN.lower()}_rank_30m.csv"
)

#==========================================================
#Part 8 Rank Analysis 60m
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
print(rank_60m.round(3))

rank_60m.to_csv(
    f"{FACTOR_COLUMN.lower()}_rank_60m.csv"
)