# NoorQuant Threshold Optimization

## Summary

- Combination #1 : **VWAP_Distance + ORB_Range + RS_15**
- Factors Tested : **VWAP_Distance, ORB_Range, RS_15**
- Timeframe : **60 Min**
- Rank : **10**
- Best Filter : **ORB_Range<18.9**
- Best Score : **0.329**

---

## Results

| Combination                       | Factor        | Filter                |    60 |   120 |   180 |   365 |    730 |   Score |   Trades |   Coverage |   Win Rate |   Avg Return |   Rank |
|:----------------------------------|:--------------|:----------------------|------:|------:|------:|------:|-------:|--------:|---------:|-----------:|-----------:|-------------:|-------:|
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<18.9        | 0.386 | 0.41  | 0.283 | 0.096 |  0.069 |   0.329 |       20 |       3.44 |      70    |        0.386 |      1 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<21.4        | 0.421 | 0.387 | 0.241 | 0.09  |  0.054 |   0.325 |       21 |       3.29 |      71.43 |        0.421 |      2 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<24.75       | 0.402 | 0.338 | 0.2   | 0.068 |  0.033 |   0.292 |       22 |       3.16 |      68.18 |        0.402 |      3 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.4648         | 0.414 | 0.309 | 0.199 | 0.092 |  0.017 |   0.291 |       35 |       4.23 |      62.86 |        0.414 |      4 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.13   | 0.407 | 0.297 | 0.203 | 0.083 |  0.031 |   0.285 |       33 |       4.38 |      66.67 |        0.407 |      5 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.0835  | 0.394 | 0.298 | 0.206 | 0.104 |  0.005 |   0.284 |       21 |       2.8  |      52.38 |        0.394 |      6 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.0972 | 0.419 | 0.265 | 0.182 | 0.066 |  0.017 |   0.273 |       31 |       4.44 |      67.74 |        0.419 |      7 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.1678 | 0.39  | 0.29  | 0.183 | 0.072 |  0.012 |   0.271 |       34 |       4.21 |      64.71 |        0.39  |      8 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.6056         | 0.381 | 0.289 | 0.179 | 0.08  |  0.013 |   0.268 |       36 |       4.05 |      61.11 |        0.381 |      9 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<29.1275     | 0.402 | 0.288 | 0.159 | 0.056 |  0.023 |   0.267 |       22 |       2.95 |      68.18 |        0.402 |     10 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.7895         | 0.381 | 0.278 | 0.184 | 0.08  |  0.022 |   0.266 |       36 |       3.77 |      61.11 |        0.381 |     11 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-1.0627         | 0.374 | 0.276 | 0.184 | 0.081 |  0.024 |   0.262 |       37 |       3.65 |      62.16 |        0.374 |     12 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<128.4825    | 0.371 | 0.265 | 0.19  | 0.078 |  0.019 |   0.259 |       37 |       3.43 |      62.16 |        0.371 |     13 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<61.6        | 0.365 | 0.265 | 0.178 | 0.073 |  0.015 |   0.254 |       34 |       3.52 |      61.76 |        0.365 |     14 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<79.5        | 0.357 | 0.267 | 0.181 | 0.077 |  0.008 |   0.253 |       35 |       3.39 |      62.86 |        0.357 |     15 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-1.5985         | 0.352 | 0.266 | 0.179 | 0.077 |  0.023 |   0.25  |       38 |       3.5  |      60.53 |        0.352 |     16 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.1664  | 0.328 | 0.284 | 0.192 | 0.07  |  0.01  |   0.249 |       27 |       3.15 |      55.56 |        0.328 |     17 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.2064 | 0.361 | 0.267 | 0.162 | 0.066 |  0.011 |   0.249 |       35 |       4.08 |      62.86 |        0.361 |     18 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.2436         | 0.336 | 0.265 | 0.177 | 0.081 |  0.013 |   0.245 |       34 |       4.68 |      61.76 |        0.336 |     19 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.3068 | 0.352 | 0.251 | 0.164 | 0.066 |  0.017 |   0.241 |       38 |       3.9  |      60.53 |        0.352 |     20 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.386  | 0.352 | 0.243 | 0.161 | 0.068 |  0.016 |   0.239 |       38 |       3.67 |      60.53 |        0.352 |     21 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15<0.8684          | 0.393 | 0.23  | 0.118 | 0.057 |  0.007 |   0.239 |       33 |       3.49 |      57.58 |        0.393 |     22 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.5258 | 0.352 | 0.236 | 0.157 | 0.067 |  0.01  |   0.236 |       38 |       3.46 |      60.53 |        0.352 |     23 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.4995  | 0.352 | 0.238 | 0.152 | 0.067 |  0.021 |   0.235 |       38 |       3.48 |      60.53 |        0.352 |     24 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.1241  | 0.31  | 0.251 | 0.185 | 0.078 |  0.016 |   0.232 |       26 |       3.23 |      53.85 |        0.31  |     25 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<50.3        | 0.332 | 0.254 | 0.156 | 0.057 |  0.002 |   0.232 |       33 |       3.61 |      60.61 |        0.332 |     26 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>4.6         | 0.354 | 0.218 | 0.148 | 0.077 |  0.012 |   0.231 |       34 |       3.31 |      55.88 |        0.354 |     27 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.3502         | 0.336 | 0.239 | 0.151 | 0.072 |  0.006 |   0.23  |       34 |       4.4  |      61.76 |        0.336 |     28 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.2523 | 0.323 | 0.25  | 0.158 | 0.063 |  0.012 |   0.229 |       37 |       4.03 |      59.46 |        0.323 |     29 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>2.05        | 0.348 | 0.219 | 0.154 | 0.074 |  0.011 |   0.229 |       36 |       3.35 |      58.33 |        0.348 |     30 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<34.7        | 0.335 | 0.254 | 0.133 | 0.052 |  0.015 |   0.228 |       25 |       3.11 |      64    |        0.335 |     31 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15<0.6872          | 0.369 | 0.228 | 0.101 | 0.045 |  0     |   0.224 |       27 |       3.04 |      48.15 |        0.369 |     32 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.216   | 0.323 | 0.248 | 0.146 | 0.044 |  0.002 |   0.223 |       30 |       3.25 |      56.67 |        0.323 |     33 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.0635 | 0.329 | 0.213 | 0.149 | 0.057 |  0.021 |   0.217 |       28 |       4.32 |      67.86 |        0.329 |     34 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.3524  | 0.343 | 0.21  | 0.128 | 0.052 |  0.022 |   0.216 |       36 |       3.49 |      58.33 |        0.343 |     35 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15<1.7177          | 0.352 | 0.195 | 0.126 | 0.05  |  0.018 |   0.215 |       38 |       3.52 |      60.53 |        0.352 |     36 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15<1.142           | 0.347 | 0.207 | 0.117 | 0.049 |  0.014 |   0.214 |       36 |       3.56 |      58.33 |        0.347 |     37 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15<0.5465          | 0.369 | 0.198 | 0.085 | 0.023 | -0.018 |   0.209 |       23 |       2.8  |      43.48 |        0.369 |     38 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>0.0457          | 0.267 | 0.241 | 0.171 | 0.062 |  0.01  |   0.209 |       30 |       5.09 |      60    |        0.267 |     39 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>6.9         | 0.304 | 0.188 | 0.159 | 0.081 |  0.018 |   0.207 |       32 |       3.26 |      56.25 |        0.304 |     40 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>0.0454  | 0.33  | 0.19  | 0.142 | 0.038 |  0.027 |   0.207 |       20 |       4.43 |      75    |        0.33  |     41 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range<41.5        | 0.294 | 0.229 | 0.131 | 0.047 | -0.004 |   0.205 |       28 |       3.21 |      60.71 |        0.294 |     42 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance<0.2731  | 0.303 | 0.224 | 0.122 | 0.045 |  0.017 |   0.205 |       34 |       3.46 |      55.88 |        0.303 |     43 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.1365         | 0.265 | 0.223 | 0.167 | 0.068 |  0.011 |   0.203 |       32 |       4.69 |      59.38 |        0.265 |     44 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>8.6         | 0.304 | 0.182 | 0.151 | 0.076 |  0.016 |   0.203 |       32 |       3.46 |      56.25 |        0.304 |     45 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>-0.0473         | 0.267 | 0.222 | 0.155 | 0.062 |  0.007 |   0.2   |       30 |       4.73 |      60    |        0.267 |     46 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>10.1        | 0.287 | 0.184 | 0.135 | 0.065 |  0.009 |   0.192 |       30 |       3.44 |      53.33 |        0.287 |     47 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>0.2359          | 0.211 | 0.227 | 0.185 | 0.062 |  0.001 |   0.188 |       23 |       4.72 |      65.22 |        0.211 |     48 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>14.8        | 0.328 | 0.151 | 0.092 | 0.059 | -0.007 |   0.187 |       23 |       3.26 |      56.52 |        0.328 |     49 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>11.7        | 0.295 | 0.169 | 0.122 | 0.045 | -0.004 |   0.185 |       28 |       3.44 |      53.57 |        0.295 |     50 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>0.0074  | 0.253 | 0.178 | 0.143 | 0.039 |  0.021 |   0.176 |       24 |       4.74 |      70.83 |        0.253 |     51 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>0.3271          | 0.185 | 0.214 | 0.168 | 0.077 |  0.004 |   0.174 |       22 |       5.08 |      63.64 |        0.185 |     52 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>16.7075     | 0.338 | 0.095 | 0.048 | 0.049 | -0.018 |   0.164 |       22 |       3.47 |      54.55 |        0.338 |     53 |
| VWAP_Distance + ORB_Range + RS_15 | RS_15         | RS_15>0.1368          | 0.176 | 0.19  | 0.146 | 0.057 |  0.005 |   0.156 |       26 |       4.91 |      61.54 |        0.176 |     54 |
| VWAP_Distance + ORB_Range + RS_15 | VWAP_Distance | VWAP_Distance>-0.0274 | 0.229 | 0.158 | 0.113 | 0.033 |  0.009 |   0.155 |       25 |       4.37 |      68    |        0.229 |     55 |
| VWAP_Distance + ORB_Range + RS_15 | ORB_Range     | ORB_Range>13.2        | 0.253 | 0.12  | 0.081 | 0.038 | -0.016 |   0.147 |       27 |       3.53 |      51.85 |        0.253 |     56 |