import pandas as pd
import time

from composite_rank import build_composite_rank
from research import analyze_factor

start = time.time()

# ==========================================================
# Configuration
# ==========================================================
import sys

if len(sys.argv) == 2:
    COMBINATION_NUMBER = int(sys.argv[1])
else:
    COMBINATION_NUMBER = 1

from config import COMBINATION_SIZE

leaderboard = pd.read_csv(
    f"{COMBINATION_SIZE}_factor_leaderboard.csv"
)

if COMBINATION_NUMBER < 1 or COMBINATION_NUMBER > len(leaderboard):
    print(
        f"Choose a combination between 1 and {len(leaderboard)}"
    )
    exit()

best_parameters = leaderboard.iloc[
    COMBINATION_NUMBER - 1
]

COMBINATION = [
    x.strip()
    for x in best_parameters["Combination"].split("+")
]

DATASETS = [60, 120, 180, 365, 730]

TIMEFRAMES = [
    "15 Min",
    "30 Min",
    "60 Min",
]

MAX_RANK = 30

OUTPUT_FILE = (
    f"07_parameter_optimizer_{COMBINATION_NUMBER}.csv"
)

print("=" * 80)
print("NOORQUANT PARAMETER OPTIMIZER")
print("=" * 80)
print("Combination :", " + ".join(COMBINATION))
print()

results = []

# ==========================================================
# Test Every Rank
# ==========================================================

for timeframe in TIMEFRAMES:

    print(f"\n=== {timeframe} ===")

    for rank in range(1, MAX_RANK + 1):

        print(f"\nRank {rank}")

        dataset_results = {}

        for days in DATASETS:

            master_dataset = (
                f"data/processed/{days}d_master_dataset.csv"
            )

            df = pd.read_csv(
                master_dataset,
                parse_dates=["Datetime"]
            )

            df = build_composite_rank(
                df,
                COMBINATION
            )

            result = analyze_factor(
                days=days,
                research_df=df,
                timeframe=timeframe,
                best_rank=rank,
            )

            if result is None:

                dataset_results[days] = None

                print(
                    f"  {days}d : Not enough trades"
                )

                continue

            winner = result["Winner"]

            dataset_results[days] = winner

            print(
                f"  {days}d : "
                f"{winner['Expectancy']:.3f}"
            )

        # -----------------------------------------------
        # Skip if any dataset failed
        # -----------------------------------------------

        if any(
            dataset_results[d] is None
            for d in DATASETS
        ):
            continue

        score = (
            dataset_results[60]["Expectancy"] * 0.35
            +
            dataset_results[120]["Expectancy"] * 0.30
            +
            dataset_results[180]["Expectancy"] * 0.20
            +
            dataset_results[365]["Expectancy"] * 0.15
        )

        results.append({

            "Timeframe": timeframe,
            "Rank": rank,

            "60": round(
                dataset_results[60]["Expectancy"],
                3
            ),

            "120": round(
                dataset_results[120]["Expectancy"],
                3
            ),

            "180": round(
                dataset_results[180]["Expectancy"],
                3
            ),

            "365": round(
                dataset_results[365]["Expectancy"],
                3
            ),

            "730": round(
                dataset_results[730]["Expectancy"],
                3
            ),

            "Score": round(score, 3),

            "Trades":
                dataset_results[60]["Trades"],

            "Coverage":
                round(
                    dataset_results[60]["Coverage"],
                    2
                ),

            "Win Rate":
                round(
                    dataset_results[60]["WinRate"],
                    2
                ),

            "Avg Return":
                round(
                    dataset_results[60]["AvgReturn"],
                    3
                ),

            "Median Return":
                round(
                    dataset_results[60]["MedianReturn"],
                    3
                ),
        })
        #==========================================================
# Build Leaderboard
#==========================================================

leaderboard = (
    pd.DataFrame(results)
    .sort_values(
        "Score",
        ascending=False
    )
    .reset_index(drop=True)
)

leaderboard.insert(
    0,
    "Combination",
    " + ".join(COMBINATION)
)

leaderboard["Overall Rank"] = leaderboard.index + 1

print()
print("=" * 80)
print(leaderboard.to_string(index=False))

leaderboard.to_csv(
    OUTPUT_FILE,
    index=False
)

#==========================================================
# Markdown Report
#==========================================================

md_file = OUTPUT_FILE.replace(
    ".csv",
    ".md"
)

best = leaderboard.iloc[0]

with open(md_file, "w") as f:

    f.write("# NoorQuant Parameter Optimization\n\n")

    f.write("## Summary\n\n")
    f.write(
        f"- Combination : "
        f"**{' + '.join(COMBINATION)}**\n"
    )
    f.write(
        f"- Timeframes Tested : "
        f"{len(TIMEFRAMES)}\n"
    )
    f.write(
        f"- Maximum Rank Tested : "
        f"{MAX_RANK}\n"
    )
    f.write(
        f"- Total Experiments : "
        f"{len(leaderboard)}\n\n"
    )

    f.write("---\n\n")

    f.write("## Best Parameters\n\n")

    f.write(
        f"- Timeframe : "
        f"**{best['Timeframe']}**\n"
    )
    f.write(
        f"- Rank : "
        f"**{best['Rank']}**\n"
    )
    f.write(
        f"- Score : "
        f"**{best['Score']:.3f}**\n"
    )
    f.write(
        f"- Trades : "
        f"**{best['Trades']}**\n"
    )
    f.write(
        f"- Coverage : "
        f"**{best['Coverage']:.2f}%**\n"
    )
    f.write(
        f"- Win Rate : "
        f"**{best['Win Rate']:.2f}%**\n"
    )
    f.write(
        f"- Avg Return : "
        f"**{best['Avg Return']:.3f}**\n"
    )
    f.write(
        f"- Median Return : "
        f"**{best['Median Return']:.3f}**\n\n"
    )

    f.write("---\n\n")

    f.write("## Top 20\n\n")

    f.write(
        leaderboard
        .head(20)
        .to_markdown(index=False)
    )

    f.write("\n\n---\n\n")

    f.write("## Full Leaderboard\n\n")

    f.write(
        leaderboard.to_markdown(index=False)
    )

print()
print("=" * 80)
print("BEST PARAMETERS")
print("=" * 80)
print(best)

print()
print(
    f"CSV saved to {OUTPUT_FILE}"
)
print(
    f"Markdown saved to {md_file}"
)
print(
    f"Completed in {time.time()-start:.1f} seconds"
)