# NoorQuant Threshold Optimization

## Summary

- Combination #4 : **Previous_Day_Return + RS_60 + ORB_Low**
- Factors Tested : **Previous_Day_Return, RS_60, ORB_Low**
- Timeframe : **15 Min**
- Rank : **21**
- Best Filter : **RS_60>-0.5438**
- Locked Filters : **ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438**
- Baseline Score : **0.171**
- Optimized Score : **0.176**
- Improvement : **2.80%**

---

## Results

| Combination                           | Factor   | Filter        |    60 |   120 |   180 |   365 |    730 |   Baseline |   Score |   Improvement % |   Trades |   Coverage |   Win Rate |   Avg Return | Timeframe   |   Best Rank |   Rank | Locked Filters                                                   |
|:--------------------------------------|:---------|:--------------|------:|------:|------:|------:|-------:|-----------:|--------:|----------------:|---------:|-----------:|-----------:|-------------:|:------------|------------:|-------:|:-----------------------------------------------------------------|
| Previous_Day_Return + RS_60 + ORB_Low | RS_60    | RS_60>-0.5438 | 0.264 | 0.176 | 0.11  | 0.058 | -0.016 |      0.171 |   0.176 |            2.8  |       20 |       4.58 |         70 |        0.264 | 15 Min      |          21 |      1 | ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438 |
| Previous_Day_Return + RS_60 + ORB_Low | RS_60    | RS_60>-0.6961 | 0.264 | 0.172 | 0.103 | 0.056 | -0.017 |      0.171 |   0.173 |            1.09 |       20 |       4.33 |         70 |        0.264 | 15 Min      |          21 |      2 | ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438 |
| Previous_Day_Return + RS_60 + ORB_Low | RS_60    | RS_60>-0.9006 | 0.264 | 0.172 | 0.103 | 0.053 | -0.016 |      0.171 |   0.172 |            0.85 |       20 |       4.11 |         70 |        0.264 | 15 Min      |          21 |      3 | ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438 |
| Previous_Day_Return + RS_60 + ORB_Low | RS_60    | RS_60>-1.1969 | 0.264 | 0.164 | 0.101 | 0.051 | -0.005 |      0.171 |   0.169 |           -1.02 |       20 |       3.87 |         70 |        0.264 | 15 Min      |          21 |      4 | ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438 |
| Previous_Day_Return + RS_60 + ORB_Low | RS_60    | RS_60>-1.7851 | 0.264 | 0.139 | 0.08  | 0.044 | -0.007 |      0.171 |   0.157 |           -8.4  |       20 |       3.62 |         70 |        0.264 | 15 Min      |          21 |      5 | ORB_Low<1682.9 AND Previous_Day_Return>-0.3387 AND RS_60>-0.5438 |