"""
Configuration file for Predictive Circular-Resource Grid (PCRG).
Contains file paths, sustainability assumptions, and model hyperparameters.
"""
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
DOCS_DIR = PROJECT_ROOT / "docs"
DATABASE_PATH = PROJECT_ROOT / "pcrg.db"

# Data File Names
DATA_FILES = {
    "buildings": "buildings.xlsx",
    "calendar": "calendar.xlsx",
    "hourly_streams": "hourly_streams.xlsx",
    "daily_summary": "daily_summary.xlsx",
    "manual_logs": "manual_logs.xlsx",
    "waste_events_train": "waste_events_train.xlsx",
    "waste_events_test": "waste_events_test.xlsx",
}

# Sustainability & Financial Assumptions (Configurable, clearly labeled)
ELECTRICITY_TARIFF_INR_PER_KWH = 8.0          # ₹ per kWh
ELECTRICITY_EMISSIONS_KG_CO2_PER_KWH = 0.70   # kg CO2 / kWh
WATER_PUMPING_KWH_PER_KL = 0.85               # kWh / 1000 Litres (kL)

# Avoidable waste / anomaly savings estimation percentage of excessive consumption
DEFAULT_SAVINGS_OPPORTUNITY_FACTOR = 0.65     # Fraction of off-hour/anomalous surge deemed avoidable

# Model Configurations
RANDOM_STATE = 42
DEFAULT_FORECAST_HORIZON_HOURS = 12
ANOMALY_Z_SCORE_THRESHOLD = 2.5
OFF_HOURS_START = 19  # 7 PM
OFF_HOURS_END = 6     # 6 AM
