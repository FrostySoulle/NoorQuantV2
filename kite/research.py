import pandas as pd
from config import MIN_TRADES
def analyze_timeframe(research_df, future_column):

    table = (
        research_df
        .groupby("Rank")
        .agg(
            Count=(future_column, "count"),
            Avg_Return=(future_column, "mean"),
            Median_Return=(future_column, "median"),
            Win_Rate=(
                future_column,
                lambda x: (x > 0).mean() * 100
            ),
            Avg_Win=(
                future_column,
                lambda x: x[x > 0].mean()
            ),
            Avg_Loss=(
                future_column,
                lambda x: x[x < 0].mean()
            )
        )
    )

    table["Expectancy"] = (
        (table["Win_Rate"] / 100) * table["Avg_Win"]
        +
        ((100 - table["Win_Rate"]) / 100)
        * table["Avg_Loss"]
    )

    table = table.fillna(0)

    return table

def summarize_timeframe(
    name,
    table,
    min_trades,
    total_rows,
    best_rank=None,
):

    valid = table[
        table["Count"] >= min_trades
    ]

    if valid.empty:
        print()
        print("DEBUG")
        print("Minimum Trades :", min_trades)
        print(table[["Count"]])

        return None

    if best_rank is None:

        best_rank = valid["Expectancy"].idxmax()

    else:

        if best_rank not in valid.index:
            return None

    return {
        "Timeframe": name,
        "BestRank": int(best_rank),
        "Trades": int(table.loc[best_rank, "Count"]),
        "Coverage": float(
            table.loc[best_rank, "Count"] / total_rows * 100
        ),
        "WinRate": float(table.loc[best_rank, "Win_Rate"]),
        "AvgReturn": float(table.loc[best_rank, "Avg_Return"]),
        "MedianReturn": float(
    table.loc[best_rank, "Median_Return"]
        ),
        "Expectancy": float(table.loc[best_rank, "Expectancy"]),
    }

def analyze_factor(
    days,
    factor=None,
    research_df=None,
    filters=None,
    save_rankings=False,
    save_research=False,
    timeframe=None,
    best_rank=None,
    start_date=None,
    end_date=None,
):

    if filters is None:
        filters = []

    VALID_DATASETS = {60, 120, 180, 365, 730}

    if days not in VALID_DATASETS:
        raise ValueError(
            "Dataset must be one of 60,120,180,365,730"
        )

    min_trades = MIN_TRADES[days]

    if start_date is not None or end_date is not None:

        min_trades = max(
            20,
            int(min_trades * 0.30)
        )

    if research_df is None:

        master_dataset = (
            f"data/processed/{days}d_master_dataset.csv"
        )
    
        research_df = pd.read_csv(
            master_dataset,
            parse_dates=["Datetime"]
        )

    if start_date is not None:

        start_date = pd.Timestamp(start_date)
    
        if research_df["Datetime"].dt.tz is not None:
            start_date = start_date.tz_localize(
                research_df["Datetime"].dt.tz
            )
    
        research_df = research_df[
            research_df["Datetime"] >= start_date
        ]
    
    if end_date is not None:
    
        end_date = pd.Timestamp(end_date)
    
        if research_df["Datetime"].dt.tz is not None:
            end_date = end_date.tz_localize(
                research_df["Datetime"].dt.tz
            )
    
        research_df = research_df[
            research_df["Datetime"] <= end_date
        ]
    if research_df.empty:
        raise ValueError(
            "No rows in selected date range."
    )
#==========================================================
# Apply Filters
#==========================================================

    for f in filters:

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

        if research_df.empty:
            raise ValueError(
                f"No rows remaining after filter: {f}"
            )
#==========================================================
# Rank Factor
#==========================================================

    if "Rank" not in research_df.columns:

      research_df["Rank"] = (
          research_df
          .groupby("Datetime")[factor]
          .rank(
              method="first",
              ascending=False
          )
          .astype(int)
      )
#==========================================================
# Analyze Timeframes
#==========================================================

    rank_15m = analyze_timeframe(
        research_df,
        "Future_15m"
    )

    rank_30m = analyze_timeframe(
        research_df,
        "Future_30m"
    )

    rank_60m = analyze_timeframe(
        research_df,
        "Future_60m"
    )
    
    summary = []
    summary_dict = {}
      
    for name, table in [
        ("15 Min", rank_15m),
        ("30 Min", rank_30m),
        ("60 Min", rank_60m),
    ]:

      result = summarize_timeframe(
          name,
          table,
          min_trades,
          len(research_df),
          best_rank=best_rank,
      )
  
      if result:
          summary.append(result)
          summary_dict[name] = result
    
    if not summary:
      raise ValueError(
        "No valid timeframes found."
    )

    if timeframe is None:

      winner = max(
        summary,
        key=lambda x: x["Expectancy"]
    )

    else:

      winner = summary_dict.get(timeframe)

    if winner is None:
        return None
    
    return {
        "Dataset": days,
        "Factor": factor,
        "Filters": filters,
        "Rows": len(research_df),

        "StartDate": research_df["Datetime"].min(),
        "EndDate": research_df["Datetime"].max(),
        "Dates": research_df["Datetime"].nunique(),
        "Stocks": research_df["Symbol"].nunique(),
    
        "15 Min": summary_dict.get("15 Min"),
        "30 Min": summary_dict.get("30 Min"),
        "60 Min": summary_dict.get("60 Min"),
    
        "Winner": winner,
    
        "Tables": {
            "15": rank_15m,
            "30": rank_30m,
            "60": rank_60m,
        }
    }