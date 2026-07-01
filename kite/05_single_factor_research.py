from research import analyze_factor
from config import FACTORS
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
DATASETS = [60, 120, 180, 365, 730]
KEEP_PERCENT = 0.70

results = []

for factor in FACTORS:

  print(f"\nTesting {factor}")

  factor_scores = {}
  
  for days in DATASETS:

    result = analyze_factor(
        days=days,
        factor=factor
    )
    assert result["Winner"] is not None
  
    edge = result["Winner"]["Expectancy"]
  
    factor_scores[days] = edge
    
    print(f"  ✓ {factor} | {days} Days")
  
  score = (
    factor_scores.get(60,0) * 0.35 +
    factor_scores.get(120,0) * 0.30 +
    factor_scores.get(180,0) * 0.20 +
    factor_scores.get(365,0) * 0.15
  )

  results.append({
    "Factor": factor,
    "60": round(factor_scores.get(60,0),3),
    "120": round(factor_scores.get(120,0),3),
    "180": round(factor_scores.get(180,0),3),
    "365": round(factor_scores.get(365,0),3),
    "730": round(factor_scores.get(730,0),3),
    "Score": round(score,3),
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
best_score = leaderboard.iloc[0]["Score"]

leaderboard["Qualified"] = (
    leaderboard["Score"]
    >= best_score * KEEP_PERCENT
)

leaderboard = leaderboard[
    [
        "Rank",
        "Factor",
        "60",
        "120",
        "180",
        "365",
        "730",
        "Score",
        "Qualified",
    ]
]

qualified = leaderboard[
    leaderboard["Qualified"]
]
print()
print("="*80)
print(f"FACTORS KEPT ({KEEP_PERCENT*100:.0f}% of Best Score)")
print("="*80)
print(qualified)

leaderboard.to_csv(
    "single_factor_leaderboard.csv",
    index=False
)
