NoorQuant V2 Research Roadmap

The purpose of NoorQuant V2 is to validate or reject hypotheses before building an automated trading system.

Every research task must answer one of the following questions.

---

Q0 - Universe Validity

Can the current halal universe (~30 stocks) generate enough opportunity for a long-only intraday strategy?

Measurements:

- Average setups per day
- Average setups per week
- Average setups per month
- Average liquidity
- Average traded value

Success Criteria:

Universe provides sufficient opportunity without requiring expansion.

Failure Criteria:

Too few opportunities or insufficient liquidity.

---

Q1 - Relative Strength

Which Relative Strength definition best predicts future performance?

Candidates:

- RS_Open
- RS_15
- RS_30
- RS_60

Research Goal:

Determine whether stronger stocks continue outperforming weaker stocks.

---

Q2 - Market Regime

Does market regime significantly affect performance?

Candidates:

- Bull Trend
- Bear Trend
- Sideways

Research Goal:

Determine whether trades should only be taken during specific market conditions.

---

Q3 - Opening Range Breakout

Does ORB produce positive expectancy?

Candidates:

- 5 minute ORB
- 10 minute ORB
- 15 minute ORB
- 30 minute ORB

Research Goal:

Determine which ORB definition performs best.

---

Q4 - Volume Expansion

Does volume expansion improve setup quality?

Candidates:

- 1.2x
- 1.5x
- 2.0x

Research Goal:

Determine whether abnormal volume improves continuation probability.

---

Q5 - Absolute Strength Filter

Does requiring:

- Price > Open
- Price > VWAP

improve performance compared to Relative Strength alone?

---

Q6 - Candidate Selection

How many top-ranked stocks should be monitored?

Candidates:

- Top 3
- Top 5
- Top 10
- Top 15

Research Goal:

Determine optimal candidate pool size.

---

Q7 - Exit Strategy

Which exit logic provides best expectancy?

Candidates:

- Fixed target
- ATR stop
- Trailing stop
- Time stop
- EOD exit

Research Goal:

Determine realistic trade management rules.

---

Q8 - Costs & Slippage

Does edge survive after:

- Brokerage
- STT
- Exchange Charges
- GST
- Slippage

Research Goal:

Determine whether gross profitability survives real-world execution.

---

Research Principle

No strategy rule becomes permanent until supported by evidence.