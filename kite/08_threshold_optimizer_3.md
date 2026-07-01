# NoorQuant Threshold Optimization

## Summary

- Combination #3 : **VWAP_Distance + Previous_Day_Return + Gap**
- Factors Tested : **VWAP_Distance, Previous_Day_Return, Gap**
- Timeframe : **60 Min**
- Rank : **10**
- Best Filter : **VWAP_Distance>-0.3068**
- Locked Filters : **Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068**
- Baseline Score : **0.194**
- Optimized Score : **0.207**
- Improvement : **6.47%**

---

## Results

| Combination                               | Factor        | Filter                |    60 |   120 |   180 |    365 |    730 |   Baseline |   Score |   Improvement % |   Trades |   Coverage |   Win Rate |   Avg Return | Timeframe   |   Best Rank |   Rank | Locked Filters                                                     |
|:------------------------------------------|:--------------|:----------------------|------:|------:|------:|-------:|-------:|-----------:|--------:|----------------:|---------:|-----------:|-----------:|-------------:|:------------|------------:|-------:|:-------------------------------------------------------------------|
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.3068 | 0.261 | 0.274 | 0.147 |  0.025 | -0.086 |      0.194 |   0.207 |            6.47 |       25 |       4.19 |      68    |        0.261 | 60 Min      |          10 |      1 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.13   | 0.242 | 0.266 | 0.149 |  0.02  | -0.097 |      0.194 |   0.197 |            1.62 |       20 |       4.28 |      75    |        0.242 | 60 Min      |          10 |      2 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.5258 | 0.261 | 0.26  | 0.123 |  0.012 | -0.087 |      0.194 |   0.196 |            0.85 |       25 |       3.78 |      68    |        0.261 | 60 Min      |          10 |      3 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.386  | 0.261 | 0.26  | 0.123 |  0.012 | -0.085 |      0.194 |   0.196 |            0.85 |       25 |       3.99 |      68    |        0.261 | 60 Min      |          10 |      4 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance<0.216   | 0.278 | 0.229 | 0.069 | -0.007 | -0.08  |      0.194 |   0.179 |           -7.76 |       20 |       3.63 |      65    |        0.278 | 60 Min      |          10 |      5 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.1678 | 0.209 | 0.247 | 0.141 |  0.013 | -0.103 |      0.194 |   0.177 |           -8.57 |       22 |       4.41 |      68.18 |        0.209 | 60 Min      |          10 |      6 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.2064 | 0.209 | 0.247 | 0.126 |  0.009 | -0.107 |      0.194 |   0.174 |          -10.43 |       22 |       4.2  |      68.18 |        0.209 | 60 Min      |          10 |      7 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance>-0.2523 | 0.203 | 0.241 | 0.126 |  0.01  | -0.1   |      0.194 |   0.17  |          -12.25 |       24 |       4.28 |      66.67 |        0.203 | 60 Min      |          10 |      8 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance<0.2731  | 0.234 | 0.191 | 0.044 | -0.015 | -0.075 |      0.194 |   0.146 |          -24.8  |       21 |       3.6  |      61.9  |        0.235 | 60 Min      |          10 |      9 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance<0.3524  | 0.243 | 0.176 | 0.03  | -0.028 | -0.094 |      0.194 |   0.14  |          -28.01 |       22 |       3.58 |      63.64 |        0.243 | 60 Min      |          10 |     10 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |
| VWAP_Distance + Previous_Day_Return + Gap | VWAP_Distance | VWAP_Distance<0.4995  | 0.247 | 0.162 | 0.041 | -0.022 | -0.074 |      0.194 |   0.14  |          -27.88 |       24 |       3.67 |      66.67 |        0.247 | 60 Min      |          10 |     11 | Previous_Day_Return<0.185 AND Gap<0.6289 AND VWAP_Distance>-0.3068 |