import pandas as pd

df = pd.read_csv("data/sample_portfolio.csv")

df["collection_rate"] = (
    df["actual_payment"] / df["expected_payment"]
) * 100

print(df)

summary = df.groupby("branch")[
    ["expected_payment", "actual_payment"]
].sum()

print(summary)
