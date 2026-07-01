#==========================================================
# Part 1 Imports
#==========================================================

import subprocess
import re
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

#==========================================================
# Part 2 Configuration
#==========================================================
FORCE_RERUN = True
KEEP_PERCENT = 0.70

from config import FACTORS

DATASETS = [60,120,180,365,730]

import os

if os.path.exists("single_factor_leaderboard.csv") and not FORCE_RERUN:
    leaderboard = pd.read_csv("single_factor_leaderboard.csv")
    results = leaderboard.to_dict("records")
else:
    results = []

#==========================================================
# Part 3 Run Research
#==========================================================

for factor in FACTORS:

    if (
        not FORCE_RERUN
        and any(r["Factor"] == factor for r in results)
    ):
        print(f"Skipping {factor}")
        continue

    factor_scores = {}

    for days in DATASETS:

        command = [
            "python",
            "03_factor_research.py",
            str(days),
            factor
        ]

        output = subprocess.check_output(
            command,
            text=True
        )

        print(f"✓ {factor} | {days} Days Complete")

        match = re.search(
            r"RESULT\|(\d+)\|(.+?)\|(.+?)\|([-\d.]+)",
            output
        )

        if match:

            dataset = int(match.group(1))
            edge = float(match.group(4))

            factor_scores[dataset] = edge

    score = (
      factor_scores.get(60,0)  * 0.35
      + factor_scores.get(120,0) * 0.30
      + factor_scores.get(180,0) * 0.20
      + factor_scores.get(365,0) * 0.15
    )

    results.append({
    "Factor": factor,
    "60": round(factor_scores.get(60,0), 3),
    "120": round(factor_scores.get(120,0), 3),
    "180": round(factor_scores.get(180,0), 3),
    "365": round(factor_scores.get(365,0), 3),
    "730": round(factor_scores.get(730,0), 3),
    "Score": round(score, 3)
    })
      
      
    pd.DataFrame(results) \
    .sort_values(
        "Score",
        ascending=False
    ) \
    .to_csv(
        "single_factor_leaderboard.csv",
        index=False
    )
        
#==========================================================
# Part 4 Leaderboard
#==========================================================

leaderboard = (
    pd.read_csv("single_factor_leaderboard.csv")
    .sort_values(
        "Score",
        ascending=False
    )
    .reset_index(drop=True)
)

best_score = leaderboard.iloc[0]["Score"]

qualified = leaderboard[
    leaderboard["Score"] >= best_score * KEEP_PERCENT
]

print()
print("="*80)
print("SINGLE FACTOR LEADERBOARD")
print("="*80)
print(leaderboard)
print()
print("="*80)
print(f"FACTORS KEPT ({KEEP_PERCENT*100:.0f}% of Best Score)")
print("="*80)
print(qualified)
leaderboard.to_csv(
    "single_factor_leaderboard.csv",
    index=False
)
qualified.to_csv(
    "qualified_factors.csv",
    index=False
)

print()
input("Press ENTER to continue...")