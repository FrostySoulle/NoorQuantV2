NoorQuant V2 Research Database Schema

The database stores raw evidence first, derived research second, and simulated trades last.

---

Table: market_days

One row per trading day.

Columns:

- date
- open
- high
- low
- close
- volume
- vwap
- regime
- advancers
- decliners
- stocks_above_vwap

Purpose:

Provides market context for every research observation.

---

Table: stock_bars

One row per stock per candle.

Columns:

- datetime
- symbol
- open
- high
- low
- close
- volume

Purpose:

Raw intraday data.

Never modify after ingestion.

---

Table: candidate_observations

One row per stock per evaluation time.

Columns:

- datetime
- symbol
- hypothesis_id
- metric_name
- metric_value
- metric_rank

Examples:

- H1 | RS
- H4 | RVOL
- H5 | GAP
- H6 | OPEN_STRENGTH

Purpose:

Stores every research candidate before any filters are applied.

---

Table: outcomes

Measures future performance.

Columns:

- datetime
- symbol
- return_15m
- return_30m
- return_60m
- return_eod
- mfe
- mae

Purpose:

Ground truth for every observation.

---

Table: setups

Stores setups produced by a research hypothesis.

Columns:

- datetime
- symbol
- hypothesis_id
- strategy_version
- trigger_price
- stop_loss
- target
- notes

Purpose:

Contains only observations that satisfy a hypothesis.

---

Table: trades_simulated

Stores simulated trades.

Columns:

- date
- symbol
- strategy_version
- entry_time
- exit_time
- entry_price
- exit_price
- position_size
- pnl
- brokerage
- stt
- exchange_charges
- slippage
- net_pnl
- mfe
- mae
- exit_reason

Purpose:

Trade-level validation before live deployment.

---

Research Data Rules

1. Store raw market data whenever possible.
2. Never overwrite historical research data.
3. Preserve winning and losing observations.
4. Preserve rejected candidates.
5. Preserve failed setups.
6. Store both gross and net performance.
7. Every research result must be reproducible from raw data and code.
8. Derived tables may be regenerated at any time.
9. Never manually edit research results.

---

Research Philosophy

Raw data is permanent.

Research scripts are reproducible.

Hypotheses evolve.

Evidence is never discarded.