import time
from pathlib import Path

import pandas as pd

from composite_rank import build_composite_rank
from research import analyze_factor
from config import (
    TRAIN_START,
    TRAIN_END,
    TEST_START,
    TEST_END,
    TOP_VALIDATIONS,
    WEIGHTS,
)

start = time.time()

OUTPUT_CSV = "09_validation.csv"
OUTPUT_MD = "09_validation.md"


def weighted_score(winner_by_dataset):
    score = 0.0
    for dataset, weight in WEIGHTS.items():
        score += winner_by_dataset[dataset]["Expectancy"] * weight
    return score


results = []

print("=" * 80)
print("NOORQUANT VALIDATION ENGINE")
print("=" * 80)

for number in range(1, TOP_VALIDATIONS + 1):

    threshold_file = Path(f"08_threshold_optimizer_{number}.csv")

    if not threshold_file.exists():
        continue

    leaderboard = pd.read_csv(threshold_file)
    print(leaderboard.columns.tolist())
    if leaderboard.empty:
        continue

    best = leaderboard.iloc[0]

    combination = [
        x.strip()
        for x in str(best["Combination"]).split("+")
    ]

    locked_filters = [
        x.strip()
        for x in str(best["Locked Filters"]).split("AND")
    ]

    timeframe = best["Timeframe"]
    rank = int(best["Best Rank"])
    train_score = float(best["Score"])

    print()
    print("-" * 80)
    print(f"Combination #{number}")
    print(" + ".join(combination))
    print("Filters :", " AND ".join(locked_filters))
    print("-" * 80)

    winners = {}

    failed = False

    for days in [60, 120, 180, 365, 730]:

        df = pd.read_csv(
            f"data/processed/{days}d_master_dataset.csv",
            parse_dates=["Datetime"]
        )

        df = build_composite_rank(df, combination)

        try:

            result = analyze_factor(
                days=days,
                research_df=df,
                filters=locked_filters,
                timeframe=timeframe,
                best_rank=rank,
                start_date=TEST_START,
                end_date=TEST_END,
            )

        except Exception as e:
            print(f"{days}d : FAILED ({e})")
            failed = True
            break

        winners[days] = result["Winner"]

        print(
            f"{days}d : "
            f'{result["Winner"]["Expectancy"]:.3f}'
        )

    if failed:
        continue

    validation_score = weighted_score(winners)

    drop = (
    (validation_score - train_score)
    / train_score
    * 100
    if train_score != 0
    else 0
    )
    
    retention = (
        validation_score
        / train_score
        * 100
        if train_score != 0
        else 0
    )
    
    if retention >= 100:
    
        confidence = "Outstanding"
    
    elif retention >= 95:
    
        confidence = "Excellent"
    
    elif retention >= 85:
    
        confidence = "Strong"
    
    elif retention >= 70:
    
        confidence = "Acceptable"
    
    elif retention >= 50:
    
        confidence = "Weak"
    
    else:
    
        confidence = "Reject"
    
    verdict = (
        "PASS"
        if retention >= 80
        else "FAIL"
    )

    results.append({
        "Combination #": number,
        "Combination": " + ".join(combination),
        "Locked Filters": " AND ".join(locked_filters),
        "Train Score": round(train_score, 3),
        "Validation Score": round(validation_score, 3),
        "Retention %": round(retention, 2),
        "Change %": round(drop, 2),
        "Confidence": confidence,
        "Verdict": verdict,
        "60": round(winners[60]["Expectancy"], 3),
        "120": round(winners[120]["Expectancy"], 3),
        "180": round(winners[180]["Expectancy"], 3),
        "365": round(winners[365]["Expectancy"], 3),
        "730": round(winners[730]["Expectancy"], 3),
        "Trades": winners[60]["Trades"],
        "Coverage": round(winners[60]["Coverage"], 2),
        "Win Rate": round(winners[60]["WinRate"], 2),
        "Avg Return": round(winners[60]["AvgReturn"], 3),
    })
if len(results) == 0:

    print()
    print("No strategy passed validation.")
    exit()
leaderboard = (
    pd.DataFrame(results)
    .sort_values(
        "Validation Score",
        ascending=False
    )
    .reset_index(drop=True)
)

leaderboard.index += 1

leaderboard.to_csv(
    OUTPUT_CSV,
    index=False
)

with open(OUTPUT_MD, "w") as f:

    f.write("# NoorQuant Validation\n\n")
    f.write("## Validation Window\n\n")
    f.write(
    "- Validation Rule : **Retention ≥ 80% = PASS**\n\n"
    ) 
    f.write(f"- Train : **{TRAIN_START} → {TRAIN_END}**\n")
    f.write(f"- Test : **{TEST_START} → {TEST_END}**\n\n")
    f.write("---\n\n")
    f.write(leaderboard.to_markdown(index=False))

print()
print("=" * 80)
print(leaderboard.to_string(index=False))
print("=" * 80)
print(f"CSV saved to {OUTPUT_CSV}")
print(f"Markdown saved to {OUTPUT_MD}")
print(f"Completed in {time.time()-start:.1f} seconds")