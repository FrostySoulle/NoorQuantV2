FACTORS = [
    "Gap",
    "Previous_Day_Return",
    "RVOL",
    "ORB_High",
    "ORB_Low",
    "ORB_Range",
    "ORB_Percent",
    "ORB_Body",
    "VWAP_Distance",
    "ATR_Percent",
    "EMA20_Distance",
    "RS_15",
    "RS_30",
    "RS_60",
]
TRAIN_START = "2024-07-01"
TRAIN_END   = "2025-12-31"

TEST_START  = "2026-01-01"
TEST_END    = None

TOP_VALIDATIONS = 10
DATASETS = [60, 120, 180, 365, 730]

COMBINATION_SIZE = 4

WEIGHTS = {
    60: 0.35,
    120: 0.30,
    180: 0.20,
    365: 0.15,
}

THRESHOLD_PERCENTILES = list(range(5, 100, 5))

MIN_TRADES = {
    60: 20,
    120: 30,
    180: 30,
    365: 50,
    730: 100,
}