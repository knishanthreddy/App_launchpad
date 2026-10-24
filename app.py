"""
Predictive Circular-Resource Grid (PCRG)
Main Application Entry Point.
Consolidated into 8 primary operational consoles under "LESS READING, MORE UNDERSTANDING".
"""
import sys
from pathlib import Path
import json
import streamlit as st
import pandas as pd

project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config import (
    OUTPUTS_DIR,
    ELECTRICITY_TARIFF_INR_PER_KWH,
    ELECTRICITY_EMISSIONS_KG_CO2_PER_KWH,
    WATER_PUMPING_KWH_PER_KL
)
from src.data_loader import DataLoader
from src.ui_components import inject_custom_styles

# Import 8 Modular Views
from src.views.campus_overview import render_campus_overview
from src.views.resource_intelligence import render_resource_intelligence
from src.views.forecasting_view import render_forecasting_view
from src.views.model_lab_view import render_model_lab
from src.views.anomalies_view import render_anomalies_view
from src.views.recommendations_view import render_recommendations_view
from src.views.sustainability_view import render_sustainability_view
from src.views.system_health_view import render_system_health_view

# Streamlit Page Config
st.set_page_config(
    page_title="PCRG - Campus Resource Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Enterprise Styles
inject_custom_styles()

# Cached Global Data Loader
@st.cache_data(show_spinner=False)
def load_all_dashboard_data():
    datasets = DataLoader.load_all()
    outputs = {}

    anom_file = OUTPUTS_DIR / "anomaly_report.csv"
    outputs["anomalies"] = pd.read_csv(anom_file) if anom_file.exists() else pd.DataFrame()

    rec_file = OUTPUTS_DIR / "recommendations.csv"
    outputs["recommendations"] = pd.read_csv(rec_file) if rec_file.exists() else pd.DataFrame()

    fc_file = OUTPUTS_DIR / "forecast_results.csv"
    outputs["forecasts"] = pd.read_csv(fc_file) if fc_file.exists() else pd.DataFrame()

    test_pred_file = OUTPUTS_DIR / "waste_events_test_predictions.csv"
    outputs["waste_test_preds"] = pd.read_csv(test_pred_file) if test_pred_file.exists() else pd.DataFrame()

    metrics_file = OUTPUTS_DIR / "model_metrics.json"
    if metrics_file.exists():
        try:
            with open(metrics_file, "r", encoding="utf-8") as f:
                outputs["metrics"] = json.load(f)
        except Exception:
            outputs["metrics"] = {}
    else:
        outputs["metrics"] = {}

    return datasets, outputs

datasets, outputs = load_all_dashboard_data()

# Sidebar Navigation (8 Consolidated Primary Sections)
st.sidebar.markdown("### **PCRG Intelligence Grid**")
st.sidebar.caption("AI-Powered Campus Utility & Circular Asset Management")

nav_choice = st.sidebar.radio(
    "Navigation Console",
    [
        "1. Overview",
        "2. Resources",
        "3. Forecasts",
        "4. AI Lab",
        "5. Alerts",
        "6. Recommendations",
        "7. Sustainability",
        "8. System Health"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("##### **Configurable Institutional Tariffs**")
st.sidebar.info(
    f"• **Electricity Tariff**: ₹{ELECTRICITY_TARIFF_INR_PER_KWH:.2f} / kWh\n"
    f"• **Grid Carbon Factor**: {ELECTRICITY_EMISSIONS_KG_CO2_PER_KWH:.2f} kg CO2/kWh\n"
    f"• **Pumping Energy**: {WATER_PUMPING_KWH_PER_KL:.2f} kWh / kL\n\n"
    "*(Configurable in config.py)*"
)
st.sidebar.caption("PCRG Prototype v2.0 | Offline Resilient")

# View Router
if nav_choice == "1. Overview":
    render_campus_overview(datasets, outputs)
elif nav_choice == "2. Resources":
    render_resource_intelligence(datasets, outputs)
elif nav_choice == "3. Forecasts":
    render_forecasting_view(datasets, outputs)
elif nav_choice == "4. AI Lab":
    render_model_lab(datasets, outputs)
elif nav_choice == "5. Alerts":
    render_anomalies_view(datasets, outputs)
elif nav_choice == "6. Recommendations":
    render_recommendations_view(datasets, outputs)
elif nav_choice == "7. Sustainability":
    render_sustainability_view(datasets, outputs)
elif nav_choice == "8. System Health":
    render_system_health_view(datasets, outputs)
