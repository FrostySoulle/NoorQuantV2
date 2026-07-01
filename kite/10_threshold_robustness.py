#==========================================================
# NoorQuant V2
# Phase : 10
# Engine : Threshold Robustness Engine
# Engine Version : 1.0
# Status : Stable
#
# Purpose
# Analyze robustness of optimized thresholds without
# rerunning optimization.
#
# Inputs
# 08_threshold_optimizer_*_all.csv
#
# Outputs
# 10_threshold_robustness.csv
# 10_threshold_robustness.md
#
#==========================================================

import time
from pathlib import Path

import pandas as pd

from config import TOP_VALIDATIONS

#==========================================================
# Start
#==========================================================

start = time.time()

OUTPUT_CSV = "10_threshold_robustness.csv"
OUTPUT_MD = "10_threshold_robustness.md"

REQUIRED_COLUMNS = [

    "Round",

    "Combination",

    "Timeframe",

    "Best Rank",

    "Locked Filters",

    "Factor",

    "Operator",

    "Threshold Value",

    "Filter",

    "60",

    "120",

    "180",

    "365",

    "730",

    "Baseline",

    "Score",

    "Improvement %",

    "Trades",

    "Coverage",

    "Win Rate",

    "Avg Return",

]

results = []

files_found = 0
files_processed = 0
files_failed = 0
analysis_failed = 0
total_rows = 0

print("=" * 80)
print("NOORQUANT THRESHOLD ROBUSTNESS ENGINE")
print("Version : 1.0")
print("=" * 80)

#==========================================================
# Helper Functions
#==========================================================

def robustness_rating(width95):

    if width95 >= 8:
        return "Excellent"

    if width95 >= 5:
        return "Strong"

    if width95 >= 3:
        return "Moderate"

    return "Curve Fit Risk"


def safe_round(value, digits=3):

    if pd.isna(value):
        return None

    return round(float(value), digits)

def stability_index(top_scores, bottom_scores):

    top = top_scores.mean()

    bottom = bottom_scores.mean()

    if bottom == 0:
        return 0

    return top / bottom


#==========================================================
# Process Every Optimization File
#==========================================================

for number in range(1, TOP_VALIDATIONS + 1):

    file = Path(
        f"08_threshold_optimizer_{number}_all.csv"
    )

    if not file.exists():

        print()
        print("-" * 80)
        print(file.name)
        print("Status : MISSING")
        print("-" * 80)

        files_failed += 1

        continue

    files_found += 1

    print()
    print("=" * 80)
    print(f"Processing : {file.name}")
    print("=" * 80)

    df = pd.read_csv(file)

    if df.empty:

        print("Status : EMPTY CSV")

        files_failed += 1

        continue

    missing = [

        c

        for c in REQUIRED_COLUMNS

        if c not in df.columns

    ]

    if len(missing):

        print()

        print("Missing Columns")

        for c in missing:
            print(" -", c)

        files_failed += 1

        continue

    files_processed += 1

    total_rows += len(df)

    print(
        "Rows Loaded :",
        len(df)
    )

    print(
        "Combination :",
        df.iloc[0]["Combination"]
    )

    print(
        "Timeframe :",
        df.iloc[0]["Timeframe"]
    )

    print(
        "Best Rank :",
        df.iloc[0]["Best Rank"]
    )

    print(
        "Rounds :",
        df["Round"].nunique()
    )

    print(
        "Factors :",
        df["Factor"].nunique()
    )

#==========================================================
# Analyze Every Round
#==========================================================

    rounds = sorted(
        df["Round"].unique()
    )

    for round_number in rounds:

        round_df = (
            df[
                df["Round"] == round_number
            ]
            .copy()
        )

        winner = (
            round_df
            .sort_values(
                "Score",
                ascending=False
            )
            .iloc[0]
        )

        factor = winner["Factor"]

        factor_df = (
            round_df[
                round_df["Factor"] == factor
            ]
            .copy()
        )

        factor_df = factor_df.sort_values(
            "Threshold Value"
        ).reset_index(
            drop=True
        )

        winner_index = factor_df[
            factor_df["Filter"]
            ==
            winner["Filter"]
        ].index[0]

        left_score = None

        right_score = None

        if winner_index > 0:

            left_score = float(

                factor_df.iloc[
                    winner_index - 1
                ]["Score"]

            )

        if winner_index < len(factor_df) - 1:

            right_score = float(

                factor_df.iloc[
                    winner_index + 1
                ]["Score"]

            )
            #==========================================================
# Robustness Metrics
#==========================================================

        winner_score = float(
            winner["Score"]
        )

        average_score = float(
            factor_df["Score"].mean()
        )

        median_score = float(
            factor_df["Score"].median()
        )

        std_dev = float(
            factor_df["Score"].std(ddof=0)
        )

        max_score = float(
            factor_df["Score"].max()
        )

        min_score = float(
            factor_df["Score"].min()
        )

#==========================================================
# Neighbour Analysis
#==========================================================

        neighbours = []

        if left_score is not None:
            neighbours.append(left_score)

        if right_score is not None:
            neighbours.append(right_score)

        if len(neighbours):

            neighbour_mean = (
                sum(neighbours)
                /
                len(neighbours)
            )

        else:

            neighbour_mean = winner_score

        neighbour_difference = (
            winner_score
            -
            neighbour_mean
        )

        winner_minus_median = (

            winner_score
        
            -
        
            median_score
        
        )
        
        winner_over_median = (
        
            winner_score
        
            /
        
            median_score
        
            if median_score != 0
        
            else 0
        
        )

#==========================================================
# Robust Width
#==========================================================

        width95 = len(

            factor_df[
                factor_df["Score"]
                >=
                winner_score * 0.95
            ]

        )

        width90 = len(

            factor_df[
                factor_df["Score"]
                >=
                winner_score * 0.90
            ]

        )

#==========================================================
# Stability Index
#==========================================================

        sorted_scores = (
            factor_df
            .sort_values(
                "Score"
            )
            .reset_index(
                drop=True
            )
        )

        n = len(sorted_scores)

        chunk = max(
            1,
            int(n * 0.20)
        )

        bottom20 = (
            sorted_scores
            .head(chunk)
        )

        top20 = (
            sorted_scores
            .tail(chunk)
        )

        stability = stability_index(

            top20["Score"],

            bottom20["Score"]

        )

#==========================================================
# Threshold Statistics
#==========================================================

        threshold_min = float(

            factor_df[
                "Threshold Value"
            ].min()

        )

        threshold_max = float(

            factor_df[
                "Threshold Value"
            ].max()

        )

        threshold_mean = float(

            factor_df[
                "Threshold Value"
            ].mean()

        )

        threshold_std = float(

            factor_df[
                "Threshold Value"
            ].std(ddof=0)

        )

#==========================================================
# Console Output
#==========================================================

        print()

        print(
            "-" * 50
        )

        print(
            f"Round {round_number}"
        )

        print(
            "-" * 50
        )

        print(
            "Winner Factor :",
            factor
        )

        print(
            "Winner Filter :",
            winner["Filter"]
        )

        print(
            f"Winner Score : {winner_score:.3f}"
        )

        print(
            f"Neighbour Mean : {neighbour_mean:.3f}"
        )

        print(
            f"Winner / Median : {winner_over_median:.3f}"
        )

        print(
            f"Robust Width 95 : {width95}"
        )

        print(
            f"Robust Width 90 : {width90}"
        )

        print(
            f"Stability Index : {stability:.3f}"
        )

        print(
            "Rating :",
            robustness_rating(width95)
        )

#==========================================================
# Store Results
#==========================================================

        results.append({

            "Combination #": number,

            "Combination":
            winner["Combination"],

            "Round":
            round_number,

            "Factor":
            factor,

            "Winner Filter":
            winner["Filter"],

            "Operator":
            winner["Operator"],

            "Threshold":
            winner["Threshold Value"],

            "Winner Score":
            safe_round(
                winner_score
            ),

            "Average Score":
            safe_round(
                average_score
            ),

            "Median Score":
            safe_round(
                median_score
            ),

            "Std Dev":
            safe_round(
                std_dev,
                4
            ),

            "Minimum Score":
            safe_round(
                min_score
            ),

            "Maximum Score":
            safe_round(
                max_score
            ),

            "Left Score":
            safe_round(
                left_score
            ),

            "Right Score":
            safe_round(
                right_score
            ),

            "Neighbour Mean":
            safe_round(
                neighbour_mean
            ),

            "Neighbour Difference":
            safe_round(
                neighbour_difference
            ),

            "Winner - Median":
            safe_round(
                winner_minus_median
            ),
            
            "Winner / Median":
            safe_round(
                winner_over_median,
                3
            ),

            "Robust Width 95":
            width95,

            "Robust Width 90":
            width90,

            "Threshold Mean":
            safe_round(
                threshold_mean
            ),

            "Threshold Std":
            safe_round(
                threshold_std,
                4
            ),

            "Threshold Min":
            safe_round(
                threshold_min
            ),

            "Threshold Max":
            safe_round(
                threshold_max
            ),

            "Stability Index":
            safe_round(
                stability,
                3
            ),

            "Trades":
            int(
                winner["Trades"]
            ),

            "Coverage":
            safe_round(
                winner["Coverage"],
                2
            ),

            "Win Rate":
            safe_round(
                winner["Win Rate"],
                2
            ),

            "Avg Return":
            safe_round(
                winner["Avg Return"]
            ),

            "Rating":
            robustness_rating(
                width95
            )

        })

    print()
    print("Status : SUCCESS")
    #==========================================================
# Build Leaderboard
#==========================================================

if len(results) == 0:

    print()
    print("=" * 80)
    print("No robustness results generated.")
    print("=" * 80)
    exit()

leaderboard = (
    pd.DataFrame(results)
    .sort_values(
        [
            "Rating",
            "Robust Width 95",
            "Winner / Median",
            "Winner Score",
        ],
        ascending=[
            True,
            False,
            True,
            False,
        ]
    )
    .reset_index(drop=True)
)

leaderboard.index += 1

#==========================================================
# Confidence Score
#==========================================================

confidence = []

for _, row in leaderboard.iterrows():

    score = 0

    if row["Robust Width 95"] >= 8:
        score += 35
    elif row["Robust Width 95"] >= 5:
        score += 25
    elif row["Robust Width 95"] >= 3:
        score += 15

    if row["Winner / Median"] < 1.05:
        score += 25
    
    elif row["Winner / Median"] < 1.10:
        score += 15
    
    elif row["Winner / Median"] < 1.20:
        score += 5

    if row["Std Dev"] < 0.02:
        score += 20
    elif row["Std Dev"] < 0.05:
        score += 10

    if row["Stability Index"] > 1.25:
        score += 20
    elif row["Stability Index"] > 1.10:
        score += 10

    confidence.append(score)

leaderboard.insert(
    1,
    "Confidence",
    confidence
)

#==========================================================
# Final Rating
#==========================================================

def confidence_label(score):

    if score >= 90:
        return "Exceptional"

    if score >= 75:
        return "Excellent"

    if score >= 60:
        return "Strong"

    if score >= 45:
        return "Moderate"

    return "Weak"

leaderboard["Confidence Label"] = (
    leaderboard["Confidence"]
    .apply(confidence_label)
)

#==========================================================
# Save CSV
#==========================================================

leaderboard.to_csv(
    OUTPUT_CSV,
    index=False
)

#==========================================================
# Markdown Report
#==========================================================

with open(
    OUTPUT_MD,
    "w"
) as f:

    f.write(
        "# NoorQuant Threshold Robustness\n\n"
    )

    f.write(
        "## Summary\n\n"
    )

    f.write(
        f"- Files Found : **{files_found}**\n"
    )

    f.write(
        f"- Files Processed : **{files_processed}**\n"
    )

    f.write(
        f"- Files Failed : **{files_failed}**\n"
    )
    
    print(
    f"Analysis Failed   : {analysis_failed}"
    )

    f.write(
        f"- Thresholds Analysed : **{total_rows}**\n\n"
    )

    f.write("---\n\n")

    f.write(
        "## Leaderboard\n\n"
    )

    f.write(
        leaderboard.to_markdown(
            index=False
        )
    )

    f.write("\n\n---\n\n")

    f.write(
        "## Interpretation\n\n"
    )

    for _, row in leaderboard.iterrows():

        f.write(
            f"### Combination {row['Combination #']}\n\n"
        )

        f.write(
            f"**Combination** : {row['Combination']}\n\n"
        )

        f.write(
            f"**Round** : {row['Round']}\n\n"
        )

        f.write(
            f"**Factor** : {row['Factor']}\n\n"
        )

        f.write(
            f"**Winning Filter** : {row['Winner Filter']}\n\n"
        )

        f.write(
            f"**Confidence** : {row['Confidence Label']}\n\n"
        )

        f.write(
            f"**Robust Width 95** : {row['Robust Width 95']}\n\n"
        )

        f.write(
            f"**Winner / Median** : {row['Winner / Median']:.3f}\n\n"
        )

        f.write(
            f"**Stability Index** : {row['Stability Index']}\n\n"
        )

        if row["Rating"] == "Excellent":

            f.write(
                "Interpretation: Threshold sits on a broad plateau. Low evidence of curve fitting.\n\n"
            )

        elif row["Rating"] == "Strong":

            f.write(
                "Interpretation: Threshold appears stable with good tolerance.\n\n"
            )

        elif row["Rating"] == "Moderate":

            f.write(
                "Interpretation: Some sensitivity exists. Validate carefully.\n\n"
            )

        else:

            f.write(
                "Interpretation: Narrow optimum detected. Possible curve fitting.\n\n"
            )

        f.write("---\n\n")
        #==========================================================
# ASCII Robustness Plot
#==========================================================

print()
print("=" * 80)
print("ROBUSTNESS CURVES")
print("=" * 80)

for number in range(1, TOP_VALIDATIONS + 1):

    file = Path(
        f"08_threshold_optimizer_{number}_all.csv"
    )

    if not file.exists():
        continue

    df = pd.read_csv(file)

    print()
    print("=" * 80)
    print(f"Combination {number}")
    print(df.iloc[0]["Combination"])
    print("=" * 80)

    for round_number in sorted(df["Round"].unique()):

        round_df = (
            df[
                df["Round"] == round_number
            ]
        )

        print()
        print(f"Round {round_number}")

        for factor in round_df["Factor"].unique():

            factor_df = (
                round_df[
                    round_df["Factor"] == factor
                ]
                .sort_values(
                    "Threshold Value"
                )
            )

            print()
            print(factor)

            maximum = factor_df["Score"].max()

            for _, row in factor_df.iterrows():

                stars = int(
                    (
                        row["Score"]
                        /
                        maximum
                    ) * 40
                )

                print(
                    f"{row['Threshold Value']:>10.4f} | "
                    + "█" * stars
                    + f" {row['Score']:.3f}"
                )

#==========================================================
# Console Summary
#==========================================================

print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)

print(
    f"Files Found       : {files_found}"
)

print(
    f"Files Processed   : {files_processed}"
)

print(
    f"Files Failed      : {files_failed}"
)

print(
    f"Rows Analysed     : {total_rows}"
)

print()

print("=" * 80)
print("TOP ROBUST STRATEGIES")
print("=" * 80)

columns = [

    "Combination #",

    "Round",

    "Factor",

    "Winner Filter",

    "Winner Score",

    "Robust Width 95",

    "Winner / Median",

    "Stability Index",

    "Confidence",

    "Confidence Label",

]

print(
    leaderboard[
        columns
    ].to_string(
        index=False
    )
)

print()

best = leaderboard.iloc[0]

print("=" * 80)
print("BEST THRESHOLD")
print("=" * 80)

print(
    "Combination :",
    best["Combination"]
)

print(
    "Round :",
    best["Round"]
)

print(
    "Factor :",
    best["Factor"]
)

print(
    "Filter :",
    best["Winner Filter"]
)

print(
    f"Confidence : {best['Confidence']}"
)

print(
    "Rating :",
    best["Confidence Label"]
)

print(
    f"Robust Width : {best['Robust Width 95']}"
)

print(
    f"Winner / Median : "
    f"{best['Winner / Median']:.3f}"
)
print(
    f"Stability Index : "
    f"{best['Stability Index']:.3f}"
)

print()

print("=" * 80)
print("Definition of Done")
print("=" * 80)

print("[✓] All optimization files located")
print("[✓] Required columns validated")
print("[✓] Thresholds analysed")
print("[✓] Robustness metrics calculated")
print("[✓] CSV generated")
print("[✓] Markdown generated")
print("[✓] Console summary generated")
print("[✓] Engine completed successfully")

print()

print("=" * 80)
print(f"CSV Saved      : {OUTPUT_CSV}")
print(f"Markdown Saved : {OUTPUT_MD}")
print(
    f"Completed in {time.time()-start:.2f} seconds"
)
print("=" * 80)