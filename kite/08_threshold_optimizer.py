import pandas as pd
import time

from composite_rank import build_composite_rank
from research import analyze_factor
from config import (
    DATASETS,
    THRESHOLD_PERCENTILES,
    WEIGHTS,
)
start = time.time()

#==========================================================

#Load Winning Parameters Automatically

#==========================================================
import sys
MAX_FILTERS = 3
if len(sys.argv) == 2:
    COMBINATION_NUMBER = int(sys.argv[1])
else:
    COMBINATION_NUMBER = 1

from config import COMBINATION_SIZE

leaderboard = pd.read_csv(
    f"07_parameter_optimizer_{COMBINATION_NUMBER}.csv"
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

TIMEFRAME = best_parameters["Timeframe"]
BEST_RANK = int(best_parameters["Rank"])
BASELINE_SCORE = float(best_parameters["Score"])

from config import DATASETS, THRESHOLD_PERCENTILES

OUTPUT_FILE = (
    f"08_threshold_optimizer_{COMBINATION_NUMBER}.csv"
)

#==========================================================

#TEST
#==========================================================

results = []
all_results = []

locked_filters = []
filter_history = []
#==========================================================
# Cache Datasets
#==========================================================

dataset_cache = {}

for days in DATASETS:

    df = pd.read_csv(
        f"data/processed/{days}d_master_dataset.csv",
        parse_dates=["Datetime"]
    )

    df = build_composite_rank(
        df,
        COMBINATION
    )

    dataset_cache[days] = df

print("Datasets cached.")

print("=" * 80)
print("NOORQUANT THRESHOLD OPTIMIZER")
print("=" * 80)
print(
    f"Combination #{COMBINATION_NUMBER}"
)
print(
    "Combination :",
    " + ".join(COMBINATION)
)
print("Timeframe   :", TIMEFRAME)
print("Rank        :", BEST_RANK)
print()
sample_df = pd.read_csv(
            "data/processed/730d_master_dataset.csv"
)
for round_number in range(MAX_FILTERS):

    print()
    print("=" * 80)
    print(
        f"ROUND {round_number + 1}"
    )
    print(
        "Locked Filters :",
        locked_filters
        if locked_filters
        else "None"
    )
    print("=" * 80)

    remaining_factors = [
        f
        for f in COMBINATION
        if not any(
            x.startswith(f)
            for x in locked_filters
        )
    ]

    if not remaining_factors:
        break

    for FACTOR_TO_OPTIMIZE in remaining_factors:

        print("=" * 80)
        print(f"Optimizing : {FACTOR_TO_OPTIMIZE}")
        print("=" * 80)
    
        #==========================================================
        # Calculate Thresholds
        #==========================================================
    
        thresholds = []
    
        for p in THRESHOLD_PERCENTILES:
    
            value = sample_df[
                FACTOR_TO_OPTIMIZE
            ].quantile(p / 100)
    
            thresholds.append(round(float(value), 4))
    
        thresholds = sorted(set(thresholds))
    
        print("\nThresholds")
        print(thresholds)
    
        for threshold in thresholds:
    
            for operator in [">", "<"]:
    
                filter_text = (
                    f"{FACTOR_TO_OPTIMIZE}"
                    f"{operator}"
                    f"{threshold}"
                )
    
                print(filter_text)
    
                dataset_results = {}
    
                for days in DATASETS:
    
                    df = dataset_cache[days].copy()
    
                    try:
    
                        result = analyze_factor(
                            days=days,
                            research_df=df,
                            filters=locked_filters + [filter_text],
                            timeframe=TIMEFRAME,
                            best_rank=BEST_RANK,
                        )
    
                    except ValueError:
                        dataset_results = None
                        break
    
                    if result is None:
                        dataset_results = None
                        break
    
                    winner = result["Winner"]
    
                    if winner is None:
                        dataset_results = None
                        break
    
                    dataset_results[days] = winner
    
                    print(
                        f"  {days}d : "
                        f"{winner['Expectancy']:.3f}"
                    )
    
                if dataset_results is None:
                    continue
    
                score = 0
    
                for dataset, weight in WEIGHTS.items():
    
                    score += (
                        dataset_results[dataset]["Expectancy"]
                        * weight
                    )
        
                operator = ">" if ">" in filter_text else "<"

                threshold_value = float(
                    filter_text.split(operator)[1]
                )
                
                row = {
                
                    "Round": round_number + 1,
                
                    "Combination": " + ".join(COMBINATION),
                
                    "Timeframe": TIMEFRAME,
                
                    "Best Rank": BEST_RANK,
                
                    "Locked Filters": " AND ".join(locked_filters),
                
                    "Factor": FACTOR_TO_OPTIMIZE,
                
                    "Operator": operator,
                
                    "Threshold Value": threshold_value,
                
                    "Filter": filter_text,
                
                    "60": round(dataset_results[60]["Expectancy"], 3),
                    "120": round(dataset_results[120]["Expectancy"], 3),
                    "180": round(dataset_results[180]["Expectancy"], 3),
                    "365": round(dataset_results[365]["Expectancy"], 3),
                    "730": round(dataset_results[730]["Expectancy"], 3),
                
                    "Baseline": round(BASELINE_SCORE, 3),
                
                    "Score": round(score, 3),
                
                    "Improvement %": round(
                        (
                            (score - BASELINE_SCORE)
                            / BASELINE_SCORE
                        ) * 100,
                        2
                    ),
                
                    "Trades": dataset_results[60]["Trades"],
                
                    "Coverage": round(
                        dataset_results[60]["Coverage"],
                        2
                    ),
                
                    "Win Rate": round(
                        dataset_results[60]["WinRate"],
                        2
                    ),
                
                    "Avg Return": round(
                        dataset_results[60]["AvgReturn"],
                        3
                    ),
                }
                
                results.append(row)
                
                all_results.append(row.copy())
#==========================================================

#RESULTS

#==========================================================
    if len(results) == 0:

      print()
      print("=" * 80)
      print("No further improvements found.")
      print("Stopping optimization.")
      break
  
    leaderboard = (
    pd.DataFrame(results)
    .sort_values(
    "Score",
    ascending=False
    )
    .reset_index(drop=True)
    )
  
    leaderboard["Rank"] = leaderboard.index + 1
    
    if MAX_FILTERS > 1:

        best_filter = leaderboard.iloc[0]["Filter"]
    
        locked_filters.append(best_filter)
        
        filter_history.append(best_filter)
        
        BASELINE_SCORE = leaderboard.iloc[0]["Score"]
    
        print()
        print(
            "LOCKED :",
            best_filter
        )
    
        results = []
print()
print("=" * 80)
print(leaderboard.to_string(index=False))

leaderboard.to_csv(
    OUTPUT_FILE,
    index=False
)

#==========================================================
# Save Complete Results
#==========================================================

ALL_OUTPUT_FILE = (
    OUTPUT_FILE.replace(
        ".csv",
        "_all.csv"
    )
)

pd.DataFrame(all_results).to_csv(
    ALL_OUTPUT_FILE,
    index=False
)

#==========================================================

#MARKDOWN

#==========================================================

md_file = OUTPUT_FILE.replace(".csv", ".md")

best = leaderboard.iloc[0]

with open(md_file, "w") as f:

  f.write("# NoorQuant Threshold Optimization\n\n")  
  
  f.write("## Summary\n\n")  
  f.write(
    f"- Combination #{COMBINATION_NUMBER} : "
    f"**{' + '.join(COMBINATION)}**\n"
  )
  f.write(f"- Factors Tested : **{', '.join(COMBINATION)}**\n")
  f.write(f"- Timeframe : **{TIMEFRAME}**\n")  
  f.write(f"- Rank : **{BEST_RANK}**\n")  
  f.write(f"- Best Filter : **{best['Filter']}**\n")
  f.write(
    "- Locked Filters : **"
    + " AND ".join(filter_history)
    + "**\n"
  )
  f.write(f"- Baseline Score : **{best['Baseline']:.3f}**\n")
  f.write(f"- Optimized Score : **{best['Score']:.3f}**\n")
  f.write(f"- Improvement : **{best['Improvement %']:.2f}%**\n\n")
  f.write("---\n\n")  
  
  f.write("## Results\n\n")  
  f.write(  
      leaderboard.to_markdown(index=False)  
  )

print()
print("=" * 80)
print("BEST FILTER")
print("=" * 80)
print(best)

print()
print(
    f"Improvement : "
    f"{best['Improvement %']:.2f}%"
)

print(f"\nCSV saved to {OUTPUT_FILE}")
print(f"Markdown saved to {md_file}")
print(
f"Completed in {time.time()-start:.1f} seconds"
)

