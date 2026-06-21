NoorQuant V2 Research Database

Table: market_days

One row per trading day.

Columns:

- date
- nifty_open
- nifty_high
- nifty_low
- nifty_close
- nifty_vwap
- regime
- advancers
- decliners
- stocks_above_vwap

---

Table: stock_days

One row per stock per day.

Columns:

- date
- symbol
- halal_status
- gap_percent
- open
- high
- low
- close
- volume
- avg_daily_volume
- avg_traded_value
- day_return

---

Table: rs_rankings

One row per stock per evaluation period.

Columns:

- date
- time
- symbol
- rs_open
- rs_15
- rs_30
- rs_60
- rank

---

Table: candidate_observations

Stores all monitored candidates.

Columns:

- date
- time
- symbol
- regime
- price_above_open
- price_above_vwap
- volume_ratio
- rs_rank
- orb_triggered

Purpose:

Allows comparison between setup and non-setup observations.

---

Table: setups

Stores detected setups.

Columns:

- date
- time
- symbol
- regime
- rs_rank
- breakout_type
- volume_ratio
- trigger_price

---

Table: outcomes

Measures future performance.

Columns:

- date
- time
- symbol
- return_15m
- return_30m
- return_60m
- return_eod
- gross_return
- net_return
- mfe
- mae

---

Table: trades_simulated

Stores simulated trades.

Columns:

- date
- symbol
- entry_time
- exit_time
- entry_price
- exit_price
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

Trade-level analysis and strategy validation.

---

Research Data Rules

1. Store raw data whenever possible.
2. Never overwrite historical research data.
3. Store both gross and net performance.
4. Preserve failed setups.
5. Preserve non-setups.
6. Preserve rejected candidates.

Data is cheap.

Lost evidence is expensive.