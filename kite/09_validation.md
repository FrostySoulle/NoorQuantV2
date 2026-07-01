# NoorQuant Validation

## Validation Window

- Validation Rule : **Retention ≥ 80% = PASS**

- Train : **2024-07-01 → 2025-12-31**
- Test : **2026-01-01 → None**

---

|   Combination # | Combination                                 | Locked Filters                                                     |   Train Score |   Validation Score |   Retention % |   Change % | Confidence   | Verdict   |    60 |   120 |   180 |   365 |   730 |   Trades |   Coverage |   Win Rate |   Avg Return |
|----------------:|:--------------------------------------------|:-------------------------------------------------------------------|--------------:|-------------------:|--------------:|-----------:|:-------------|:----------|------:|------:|------:|------:|------:|---------:|-----------:|-----------:|-------------:|
|               1 | ORB_Range + RS_15 + ORB_Low + ATR_Percent   | ORB_Range<21.4 AND ATR_Percent>0.3633 AND RS_15>-1.0627            |         0.493 |              0.504 |        102.31 |       2.31 | Outstanding  | PASS      | 0.708 | 0.532 | 0.288 | 0.263 | 0.263 |       20 |       5.65 |         85 |        0.708 |
|               2 | VWAP_Distance + Previous_Day_Return + RS_60 | Previous_Day_Return<-0.0058 AND RS_60<1.2435                       |         0.247 |              0.269 |        108.78 |       8.78 | Outstanding  | PASS      | 0.338 | 0.262 | 0.207 | 0.203 | 0.203 |       20 |       4.45 |         60 |        0.338 |
|               3 | VWAP_Distance + Previous_Day_Return + Gap   | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |         0.207 |              0.224 |        108.04 |       8.04 | Outstanding  | PASS      | 0.261 | 0.274 | 0.147 | 0.139 | 0.139 |       25 |       4.19 |         68 |        0.261 |
|               5 | ORB_Range + Previous_Day_Return + RS_60     | RS_60>-0.4051 AND ORB_Range>2.05 AND Previous_Day_Return<0.0746    |         0.207 |              0.221 |        106.71 |       6.71 | Outstanding  | PASS      | 0.197 | 0.274 | 0.21  | 0.185 | 0.185 |       20 |       4.93 |         60 |        0.197 |
|               4 | Previous_Day_Return + RS_60 + ORB_Low       | ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438   |         0.176 |              0.183 |        103.87 |       3.87 | Outstanding  | PASS      | 0.264 | 0.176 | 0.11  | 0.105 | 0.105 |       20 |       4.58 |         70 |        0.264 |