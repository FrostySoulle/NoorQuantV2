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

print("Rows :", len(master_df))
print("Stocks :", master_df["Symbol"].nunique())
print("Days :", master_df["Datetime"].dt.date.nunique())
#==========================================================
#Part 3 Select Factor
#==========================================================

FACTOR_COLUMN = "Gap"

print()
print("====================================")
print("Research Factor :", FACTOR_COLUMN)
print("====================================")
#==========================================================
#Part 4 Rank Factor
#==========================================================

research_df = master_df.copy()

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