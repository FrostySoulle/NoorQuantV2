import pandas as pd


def build_composite_rank(
    research_df,
    factors,
):
    """
    Creates a composite rank from multiple factors.

    Lower CompositeRank = Better Stock
    """

    df = research_df.copy()

    rank_columns = []

    for factor in factors:

        rank_col = f"{factor}_Rank"

        df[rank_col] = (
            df
            .groupby("Datetime")[factor]
            .rank(
                method="first",
                ascending=False
            )
        )

        rank_columns.append(rank_col)

    df["CompositeRank"] = (
        df[rank_columns]
        .sum(axis=1)
    )

    df["Rank"] = (
    df
    .groupby("Datetime")["CompositeRank"]
    .rank(
        method="first",
        ascending=True
    )
    .astype(int)
    )

    return df