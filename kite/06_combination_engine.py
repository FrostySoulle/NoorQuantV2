import sys
import pandas as pd
from itertools import combinations

from composite_rank import build_composite_rank
from research import analyze_factor
import time

start = time.time()
if len(sys.argv) != 2:
    print("Usage:")
    print("python 06_combination_engine.py 2")
    exit()

COMBINATION_SIZE = int(sys.argv[1])
DATASETS = [60, 120, 180, 365, 730]
if COMBINATION_SIZE < 2:
    print("Combination size must be >= 2")
    exit()
    
leaderboard = pd.read_csv("single_factor_leaderboard.csv")

factors = leaderboard[
    leaderboard["Qualified"]
  ]["Factor"].tolist()

if COMBINATION_SIZE > len(factors):
    print(
        f"Only {len(factors)} qualified factors available."
    )
    exit()
    
OUTPUT_FILE = (
    f"{COMBINATION_SIZE}_factor_leaderboard.csv"
)

all_combinations = list(
    combinations(
        factors,
        COMBINATION_SIZE
    )
)

print(
    f"{len(all_combinations)} combinations found."
)
print(f"Combination Size : {COMBINATION_SIZE}")

#==========================================================
# Part 5 Test Every Combination
#==========================================================

results = []

for i, combo in enumerate(
    all_combinations,
    start=1
):

    print(
        f"\n[{i}/{len(all_combinations)}] "
        f"Testing: {' + '.join(combo)}"
    )

    combo_scores = {}

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
          combo
      )
      
      result = analyze_factor(
          days=days,
          research_df=df
      )
      
      winner = result["Winner"]

      combo_scores[days] = winner
      
      edge = winner["Expectancy"]
      
      print(
          f"  ✓ {days} Days : {edge:.3f}"
      )
    
    score = (
    combo_scores[60]["Expectancy"] * 0.35 +
    combo_scores[120]["Expectancy"] * 0.30 +
    combo_scores[180]["Expectancy"] * 0.20 +
    combo_scores[365]["Expectancy"] * 0.15
    ) 

    best = max(
      combo_scores.values(),
      key=lambda x: x["Expectancy"]
    )

    results.append({

      "Combination": " + ".join(combo),
  
      "60": round(combo_scores[60]["Expectancy"],3),
      "120": round(combo_scores[120]["Expectancy"],3),
      "180": round(combo_scores[180]["Expectancy"],3),
      "365": round(combo_scores[365]["Expectancy"],3),
      "730": round(combo_scores[730]["Expectancy"],3),
  
      "Score": round(score,3),
  
      "Winner TF": best["Timeframe"],
      "Best Rank": best["BestRank"],
      "Trades": best["Trades"],
      "Coverage": round(best["Coverage"],2),
      "Win Rate": round(best["WinRate"],2),
      "Avg Return": round(best["AvgReturn"],3),
    })
    
leaderboard = (
    pd.DataFrame(results)
    .sort_values(
        "Score",
        ascending=False
    )
    .reset_index(drop=True)
)

leaderboard["Rank"] = leaderboard.index + 1

print()
print("=" * 80)
print("COMBINATION LEADERBOARD")
print("=" * 80)
print(leaderboard.to_string(index=False))

leaderboard.to_csv(
    OUTPUT_FILE,
    index=False
)

#==========================================================
# Save Markdown Report
#==========================================================

md_file = OUTPUT_FILE.replace(".csv", ".md")

best = leaderboard.iloc[0]

with open(md_file, "w") as f:

    f.write("# NoorQuant Combination Research\n\n")

    f.write("## Summary\n\n")
    f.write(f"- Combination Size : {COMBINATION_SIZE}\n")
    f.write(f"- Qualified Factors : {len(factors)}\n")
    f.write(f"- Total Combinations : {len(all_combinations)}\n")
    f.write(f"- Best Combination : **{best['Combination']}**\n")
    f.write(f"- Best Score : **{best['Score']:.3f}**\n\n")

    f.write("---\n\n")

    f.write("## Top 10 Combinations\n\n")
    f.write(
        leaderboard
        .head(10)
        .to_markdown(index=False)
    )

    f.write("\n\n---\n\n")

    f.write("## Full Leaderboard\n\n")
    f.write(
        leaderboard.to_markdown(index=False))

print(f"\nMarkdown report saved to {md_file}")
print(
    f"Completed in {time.time()-start:.1f} seconds"
)