NoorQuant Version : 2.0
Research Engine: v1.0
Last Updated: 28/6/2026

NoorQuant V2 Master Context

Project Mission

NoorQuant V2 is a hypothesis-driven quantitative research platform for long-only trading in halal Indian equities.

The objective is to validate or reject trading hypotheses using statistical evidence before constructing an automated trading system.

The system prioritizes research over optimisation.

---

Current Status

Phase: Research

Validated Strategy:
None

## Current Champion Models

### 🥇 4-Factor Champion

Status:
Current Overall Champion

Combination

- ORB_Range
- RS_15
- ORB_Low
- ATR_Percent

Timeframe:
60 Min

Rank:
15

Optimized Filters

- ORB_Range < 21.4
- ATR_Percent > 0.3633
- RS_15 > -1.0627

Weighted Score:
0.493

Win Rate:
85%

Trades:
20

## Research Records

Best Single Factor:
None

Best 3-Factor Model:
VWAP_Distance + ORB_Range + RS_15
Score: 0.330

Best 4-Factor Model:
ORB_Range + RS_15 + ORB_Low + ATR_Percent
Score: 0.493

Status:
Pending Model Validation

---

### 🥈 3-Factor Champion

Status:
Best 3-Factor Model

Combination

- VWAP_Distance
- ORB_Range
- RS_15

Timeframe:
60 Min

Rank:
10

Optimized Filters

- ORB_Range < 18.9
- VWAP_Distance > -0.2523
- RS_15 > -1.5985

Weighted Score:
0.330

Win Rate:
70%

Trades:
20

Status:
Pending Model Validation
Status
Research Candidate
(Not yet validated)

Research Engine:
Completed (v1.0)

---

Completed Research

H1 - Individual Factor Predictive Power

Status:
Completed

Conclusion:

Individual factors alone do not consistently produce sufficient predictive edge.

Several factors become useful only when combined with others.

---

H4 - Relative Volume

Status:
Rejected (Standalone)

Future Research

Investigate RVOL as:

• Trade Filter
• Market Regime Filter
• Liquidity Filter
---

Active Research

H0 - Universe Validity

H2 - Market Regime

H3 - Opening Range Breakout

H5 - Gap %

H6 - Absolute Strength Filter

H7 - Multi-Factor Model Constructionch

H8 - Threshold Optimization
Status:
In Progress

H9 - Model Validation
Status:
Planned
---

Research Engine

Current Features

- Dynamic halal universe
- Yahoo Finance data download
- Automatic retry logic
- 15-minute data
- Forward returns (15m, 30m, 60m)
- Ranking engine
- Count
- Average Return
- Median Return
- Win Rate
- Average Win
- Average Loss
- Expectancy

• Automatic factor combinations
• Composite ranking engine
• Threshold optimization
• Sequential filter optimization
• Weighted multi-dataset scoring
• Markdown report generation
• CSV report generation

---

Project Philosophy

Every hypothesis must be validated using evidence.

Rejected hypotheses are considered successful research outcomes.

No trading rule becomes permanent without statistical validation.

Optimization is permitted only after a statistical edge has been demonstrated.

---

Project Structure

Root

- database_schema.md
- decision_log.md
- hypothesis.md
- validated_strategy.md
- MASTER_CONTEXT.md

Hypothesis Folder

- hypothesis.md
- research_question.md
- conclusion.md
- research script
- generated CSV files

---

Next Research Priority

1. Validate Current Champion Model

• Factor contribution
• Rank sensitivity
• Timeframe sensitivity
• Walk-forward stability

2. Market Regime Detection

3. Relative Volume Reassessment

4. Candidate Selection Engine

5. Strategy Construction
-----

Research Pipeline

01 Universe Construction

02 Dataset Creation

03 Individual Factor Analysis

04 Multi-Factor Combination Search

05 Parameter Optimization

06 Threshold Optimization

07 Model Validation

08 Strategy Construction

09 Paper Trading

10 Live Deployment