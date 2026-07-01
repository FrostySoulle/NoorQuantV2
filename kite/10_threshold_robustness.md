# NoorQuant Threshold Robustness

## Summary

- Files Found : **5**
- Files Processed : **5**
- Files Failed : **5**
- Thresholds Analysed : **421**

---

## Leaderboard

|   Combination # |   Confidence | Combination                                 |   Round | Factor              | Winner Filter               | Operator   |   Threshold |   Winner Score |   Average Score |   Median Score |   Std Dev |   Minimum Score |   Maximum Score |   Left Score |   Right Score |   Neighbour Mean |   Neighbour Difference |   Winner - Median |   Winner / Median |   Robust Width 95 |   Robust Width 90 |   Threshold Mean |   Threshold Std |   Threshold Min |   Threshold Max |   Stability Index |   Trades |   Coverage |   Win Rate |   Avg Return | Rating         | Confidence Label   |
|----------------:|-------------:|:--------------------------------------------|--------:|:--------------------|:----------------------------|:-----------|------------:|---------------:|----------------:|---------------:|----------:|----------------:|----------------:|-------------:|--------------:|-----------------:|-----------------------:|------------------:|------------------:|------------------:|------------------:|-----------------:|----------------:|----------------:|----------------:|------------------:|---------:|-----------:|-----------:|-------------:|:---------------|:-------------------|
|               1 |           45 | ORB_Range + RS_15 + ORB_Low + ATR_Percent   |       3 | RS_15               | RS_15>-1.0627               | >          |     -1.0627 |          0.493 |           0.482 |          0.482 |    0.0105 |           0.472 |           0.493 |        0.472 |       nan     |            0.472 |                  0.021 |             0.011 |             1.022 |                 2 |                 2 |           -1.331 |          0.2679 |          -1.599 |          -1.063 |             1.044 |       20 |       5.65 |      85    |        0.708 | Curve Fit Risk | Moderate           |
|               3 |           45 | VWAP_Distance + Previous_Day_Return + Gap   |       2 | Gap                 | Gap<0.6289                  | <          |      0.6289 |          0.194 |           0.169 |          0.171 |    0.0168 |           0.13  |           0.194 |        0.13  |         0.151 |            0.141 |                  0.053 |             0.023 |             1.135 |                 2 |                 6 |            0.057 |          0.5671 |          -1.008 |           1.166 |             1.359 |       25 |       3.69 |      68    |        0.261 | Curve Fit Risk | Moderate           |
|               3 |           35 | VWAP_Distance + Previous_Day_Return + Gap   |       3 | VWAP_Distance       | VWAP_Distance>-0.3068       | >          |     -0.3068 |          0.207 |           0.175 |          0.177 |    0.0228 |           0.14  |           0.207 |        0.196 |         0.17  |            0.183 |                  0.024 |             0.03  |             1.169 |                 2 |                 4 |           -0.058 |          0.3204 |          -0.526 |           0.499 |             1.443 |       25 |       4.19 |      68    |        0.261 | Curve Fit Risk | Weak               |
|               3 |           40 | VWAP_Distance + Previous_Day_Return + Gap   |       1 | Previous_Day_Return | Previous_Day_Return<0.185   | <          |      0.185  |          0.177 |           0.136 |          0.129 |    0.0183 |           0.11  |           0.177 |        0.169 |         0.168 |            0.169 |                  0.008 |             0.048 |             1.372 |                 2 |                 3 |           -0.01  |          0.2227 |          -0.462 |           0.458 |             1.456 |       31 |       3.69 |      64.52 |        0.227 | Curve Fit Risk | Weak               |
|               5 |           35 | ORB_Range + Previous_Day_Return + RS_60     |       2 | ORB_Range           | ORB_Range>2.05              | >          |      2.05   |          0.182 |           0.167 |          0.164 |    0.0068 |           0.163 |           0.182 |      nan     |         0.163 |            0.163 |                  0.019 |             0.018 |             1.11  |                 1 |                 5 |           60.572 |         38.4388 |           2.05  |         128.482 |             1.117 |       20 |       2.71 |      60    |        0.197 | Curve Fit Risk | Weak               |
|               5 |           35 | ORB_Range + Previous_Day_Return + RS_60     |       3 | Previous_Day_Return | Previous_Day_Return<0.0746  | <          |      0.0746 |          0.207 |           0.184 |          0.181 |    0.0093 |           0.179 |           0.207 |      nan     |         0.179 |            0.179 |                  0.028 |             0.026 |             1.144 |                 1 |                 1 |            0.217 |          0.1243 |           0.075 |           0.458 |             1.156 |       20 |       4.93 |      60    |        0.197 | Curve Fit Risk | Weak               |
|               1 |           20 | ORB_Range + RS_15 + ORB_Low + ATR_Percent   |       1 | ORB_Range           | ORB_Range<21.4              | <          |     21.4    |          0.378 |           0.265 |          0.268 |    0.0564 |           0.189 |           0.378 |        0.239 |         0.322 |            0.28  |                  0.098 |             0.11  |             1.41  |                 1 |                 1 |           31.112 |         31.2986 |           2.05  |         128.482 |             1.819 |       23 |       3.6  |      78.26 |        0.581 | Curve Fit Risk | Weak               |
|               4 |           30 | Previous_Day_Return + RS_60 + ORB_Low       |       1 | ORB_Low             | ORB_Low<1682.9              | <          |   1682.9    |          0.163 |           0.089 |          0.096 |    0.0442 |           0.016 |           0.163 |        0.151 |         0.144 |            0.147 |                  0.016 |             0.067 |             1.698 |                 1 |                 2 |         2352.74  |       1896.52   |         173.922 |        6943.48  |             6.361 |       24 |       3.72 |      75    |        0.253 | Curve Fit Risk | Weak               |
|               2 |           20 | VWAP_Distance + Previous_Day_Return + RS_60 |       1 | Previous_Day_Return | Previous_Day_Return<-0.0058 | <          |     -0.0058 |          0.24  |           0.127 |          0.129 |    0.0716 |           0.015 |           0.24  |        0.017 |         0.202 |            0.11  |                  0.13  |             0.111 |             1.86  |                 1 |                 1 |           -0.01  |          0.2227 |          -0.462 |           0.458 |            12.151 |       20 |       4.16 |      60    |        0.338 | Curve Fit Risk | Weak               |
|               5 |           30 | ORB_Range + Previous_Day_Return + RS_60     |       1 | RS_60               | RS_60>-0.4051               | >          |     -0.4051 |          0.163 |           0.063 |          0.054 |    0.0362 |          -0.006 |           0.163 |        0.113 |        -0.006 |            0.053 |                  0.11  |             0.109 |             3.019 |                 1 |                 1 |            0.049 |          0.8679 |          -1.785 |           1.847 |             6.833 |       21 |       2.67 |      61.9  |        0.203 | Curve Fit Risk | Weak               |
|               4 |           70 | Previous_Day_Return + RS_60 + ORB_Low       |       3 | RS_60               | RS_60>-0.5438               | >          |     -0.5438 |          0.176 |           0.169 |          0.172 |    0.0066 |           0.157 |           0.176 |        0.173 |       nan     |            0.173 |                  0.003 |             0.004 |             1.023 |                 4 |                 4 |           -1.025 |          0.4387 |          -1.785 |          -0.544 |             1.121 |       20 |       4.58 |      70    |        0.264 | Moderate       | Strong             |
|               4 |           70 | Previous_Day_Return + RS_60 + ORB_Low       |       2 | Previous_Day_Return | Previous_Day_Return>-0.3387 | >          |     -0.3387 |          0.171 |           0.146 |          0.163 |    0.0236 |           0.11  |           0.171 |        0.163 |         0.12  |            0.142 |                  0.029 |             0.008 |             1.049 |                 4 |                 4 |            0.077 |          0.3181 |          -0.462 |           0.458 |             1.555 |       20 |       3.42 |      70    |        0.264 | Moderate       | Strong             |
|               2 |           60 | VWAP_Distance + Previous_Day_Return + RS_60 |       2 | RS_60               | RS_60<1.2435                | <          |      1.2435 |          0.247 |           0.245 |          0.247 |    0.0028 |           0.241 |           0.247 |        0.241 |         0.247 |            0.244 |                  0.003 |             0     |             1     |                 3 |                 3 |            1.347 |          0.3729 |           0.951 |           1.847 |             1.025 |       20 |       4.45 |      60    |        0.338 | Moderate       | Strong             |
|               1 |           40 | ORB_Range + RS_15 + ORB_Low + ATR_Percent   |       2 | ATR_Percent         | ATR_Percent>0.3633          | >          |      0.3633 |          0.441 |           0.404 |          0.391 |    0.0239 |           0.38  |           0.441 |        0.441 |         0.41  |            0.425 |                  0.016 |             0.05  |             1.129 |                 3 |                 4 |            0.358 |          0.1401 |           0.236 |           0.759 |             1.156 |       21 |       5.15 |      80.95 |        0.649 | Moderate       | Weak               |

---

## Interpretation

### Combination 1

**Combination** : ORB_Range + RS_15 + ORB_Low + ATR_Percent

**Round** : 3

**Factor** : RS_15

**Winning Filter** : RS_15>-1.0627

**Confidence** : Moderate

**Robust Width 95** : 2

**Winner / Median** : 1.022

**Stability Index** : 1.044

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 3

**Combination** : VWAP_Distance + Previous_Day_Return + Gap

**Round** : 2

**Factor** : Gap

**Winning Filter** : Gap<0.6289

**Confidence** : Moderate

**Robust Width 95** : 2

**Winner / Median** : 1.135

**Stability Index** : 1.359

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 3

**Combination** : VWAP_Distance + Previous_Day_Return + Gap

**Round** : 3

**Factor** : VWAP_Distance

**Winning Filter** : VWAP_Distance>-0.3068

**Confidence** : Weak

**Robust Width 95** : 2

**Winner / Median** : 1.169

**Stability Index** : 1.443

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 3

**Combination** : VWAP_Distance + Previous_Day_Return + Gap

**Round** : 1

**Factor** : Previous_Day_Return

**Winning Filter** : Previous_Day_Return<0.185

**Confidence** : Weak

**Robust Width 95** : 2

**Winner / Median** : 1.372

**Stability Index** : 1.456

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 5

**Combination** : ORB_Range + Previous_Day_Return + RS_60

**Round** : 2

**Factor** : ORB_Range

**Winning Filter** : ORB_Range>2.05

**Confidence** : Weak

**Robust Width 95** : 1

**Winner / Median** : 1.110

**Stability Index** : 1.117

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 5

**Combination** : ORB_Range + Previous_Day_Return + RS_60

**Round** : 3

**Factor** : Previous_Day_Return

**Winning Filter** : Previous_Day_Return<0.0746

**Confidence** : Weak

**Robust Width 95** : 1

**Winner / Median** : 1.144

**Stability Index** : 1.156

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 1

**Combination** : ORB_Range + RS_15 + ORB_Low + ATR_Percent

**Round** : 1

**Factor** : ORB_Range

**Winning Filter** : ORB_Range<21.4

**Confidence** : Weak

**Robust Width 95** : 1

**Winner / Median** : 1.410

**Stability Index** : 1.819

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 4

**Combination** : Previous_Day_Return + RS_60 + ORB_Low

**Round** : 1

**Factor** : ORB_Low

**Winning Filter** : ORB_Low<1682.9

**Confidence** : Weak

**Robust Width 95** : 1

**Winner / Median** : 1.698

**Stability Index** : 6.361

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 2

**Combination** : VWAP_Distance + Previous_Day_Return + RS_60

**Round** : 1

**Factor** : Previous_Day_Return

**Winning Filter** : Previous_Day_Return<-0.0058

**Confidence** : Weak

**Robust Width 95** : 1

**Winner / Median** : 1.860

**Stability Index** : 12.151

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 5

**Combination** : ORB_Range + Previous_Day_Return + RS_60

**Round** : 1

**Factor** : RS_60

**Winning Filter** : RS_60>-0.4051

**Confidence** : Weak

**Robust Width 95** : 1

**Winner / Median** : 3.019

**Stability Index** : 6.833

Interpretation: Narrow optimum detected. Possible curve fitting.

---

### Combination 4

**Combination** : Previous_Day_Return + RS_60 + ORB_Low

**Round** : 3

**Factor** : RS_60

**Winning Filter** : RS_60>-0.5438

**Confidence** : Strong

**Robust Width 95** : 4

**Winner / Median** : 1.023

**Stability Index** : 1.121

Interpretation: Some sensitivity exists. Validate carefully.

---

### Combination 4

**Combination** : Previous_Day_Return + RS_60 + ORB_Low

**Round** : 2

**Factor** : Previous_Day_Return

**Winning Filter** : Previous_Day_Return>-0.3387

**Confidence** : Strong

**Robust Width 95** : 4

**Winner / Median** : 1.049

**Stability Index** : 1.555

Interpretation: Some sensitivity exists. Validate carefully.

---

### Combination 2

**Combination** : VWAP_Distance + Previous_Day_Return + RS_60

**Round** : 2

**Factor** : RS_60

**Winning Filter** : RS_60<1.2435

**Confidence** : Strong

**Robust Width 95** : 3

**Winner / Median** : 1.000

**Stability Index** : 1.025

Interpretation: Some sensitivity exists. Validate carefully.

---

### Combination 1

**Combination** : ORB_Range + RS_15 + ORB_Low + ATR_Percent

**Round** : 2

**Factor** : ATR_Percent

**Winning Filter** : ATR_Percent>0.3633

**Confidence** : Weak

**Robust Width 95** : 3

**Winner / Median** : 1.129

**Stability Index** : 1.156

Interpretation: Some sensitivity exists. Validate carefully.

---

