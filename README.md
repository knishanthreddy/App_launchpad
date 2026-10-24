# Predictive Circular-Resource Grid (PCRG)
### AI-Powered Campus Resource Intelligence & Decision Support System

The **Predictive Circular-Resource Grid (PCRG)** is a production-grade campus resource intelligence system that monitors building electricity consumption, water usage, operational schedules, and smart-bin solid waste events. It automatically identifies wasteful base loads, forecasts multi-hour utility demand, classifies IoT bin waste events into circular material streams, generates prioritized facility maintenance recommendations, and visualizes comprehensive analytics across an interactive Streamlit dashboard.

---

## 📁 Project Architecture

```
SRUJANA/
├── app.py                     # Streamlit interactive multi-page dashboard
├── config.py                  # System paths, financial assumptions, model configurations
├── requirements.txt           # Python dependency specifications
├── README.md                  # System overview and operational guide
├── run_project.bat            # Windows one-click operational launcher
├── pcrg.db                    # Local SQLite database (offline resilience)
│
├── src/                       # Modular source code
│   ├── __init__.py
│   ├── data_loader.py         # Resilient Excel loader with path caching
│   ├── data_validation.py     # Schema, ID, and range validation
│   ├── data_integration.py    # Cross-dataset relational integration
│   ├── preprocessing.py       # Imputation, timestamp parsing, alias resolution
│   ├── feature_engineering.py # Lag features, rolling statistics, cyclical encodings
│   ├── waste_classifier.py    # Multi-class IoT bin classifier (RandomForest)
│   ├── forecasting.py         # Multi-hour resource forecasting (HistGradientBoosting)
│   ├── anomaly_detection.py   # Multi-criteria anomaly detection engine
│   ├── root_cause_analysis.py # Evidence-grounded root-cause diagnostics
│   ├── recommendation_engine.py # Prioritized facility recommendations & ROI
│   ├── circular_resources.py  # Circular diversion & material recovery analytics
│   ├── sustainability_score.py # Building sustainability scoring model
│   ├── database.py            # SQLite schema initialization and storage
│   ├── reporting.py           # Campus summaries and leaderboard generation
│   ├── model_lab.py           # Model Lab ML engines, pipelines, metrics & registry
│   └── model_lab_ui.py        # Streamlit interactive UI for Model Lab tabs
│
├── scripts/
│   ├── inspect_data.py        # Automated dataset inspection and report generator
│   └── train_models.py        # Complete end-to-end retraining & execution pipeline
│
├── data/
│   ├── raw/                   # Raw data storage
│   └── processed/             # Cleaned & integrated CSV datasets
│
├── models/
│   └── waste_classifier.joblib # Trained serialization of RandomForest pipeline
│
├── outputs/                   # Standardized deliverables & artifacts
│   ├── data_inspection_report.txt
│   ├── model_metrics.json
│   ├── waste_events_test_predictions.csv
│   ├── anomaly_report.csv
│   ├── recommendations.csv
│   └── forecast_results.csv
│
├── tests/
│   └── test_pipeline.py       # Automated unit and integration test suite
│
└── docs/
    └── project_report.md      # In-depth technical evaluation & research report
```

---

## 📊 Dataset Placement & Schema

All raw Excel files are located in the project root directory or `data/raw/`:
1. `buildings.xlsx`: 8 campus facilities (`B01` - `B08`) with area, capacity, floors, and solar attributes.
2. `calendar.xlsx`: 120-day operational calendar with event tags and weather telemetry.
3. `hourly_streams.xlsx`: 23,192 hourly records across electricity, water, solar, and footfall.
4. `daily_summary.xlsx`: 960 daily records tracking utility consumption and 6 waste sub-streams.
5. `manual_logs.xlsx`: 415 operator maintenance records with natural language log notes.
6. `waste_events_train.xlsx`: 6,314 smart bin IoT sensor readings with ground-truth classes.
7. `waste_events_test.xlsx`: 1,601 unlabelled test events.

---

## 🚀 Installation & Setup

1. **Environment Requirements**:
   - Python 3.10+ (Verified on Python 3.11.9)
   - Windows 10/11 or Linux / macOS

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Exact Commands to Run

### 1. Launch the Interactive Dashboard
```bash
streamlit run app.py
```
*Access the UI in your browser at `http://localhost:8501`.*

### 2. Retrain All AI Models & Re-run Full Pipeline
```bash
python scripts/train_models.py
```

### 3. Run Automated Test Suite
```bash
python tests/test_pipeline.py
```

### 4. Inspect Datasets
```bash
python scripts/inspect_data.py
```

### 5. Windows One-Click Execution
Double-click `run_project.bat` to launch the menu options.

---

## 🧠 Model Architectures & Empirical Metrics

### A. IoT Smart Bin Waste Classifier
- **Model**: `RandomForestClassifier` with balanced class weights.
- **Features**: Sensor telemetry (`weight_g`, `moisture_pct`, `metal_signal`, `transparency`, `acoustic_hardness`, `hour`, `day_of_week`), bin and building spatial encodings.
- **Empirical Measured Metrics (Stratified 80/20 Validation)**:
  - **Accuracy**: **85.75%**
  - **Macro-F1**: **0.8457**
  - **Macro-Precision**: **0.8838**
  - **Macro-Recall**: **0.8220**
  - **Weighted-F1**: **0.8570**
- **Test Set Inference**: 1,601 test records predicted preserving row ordering and saved to `outputs/waste_events_test_predictions.csv`.

### B. Resource Forecasting
- **Model**: `HistGradientBoostingRegressor` with chronological lag features ($t-1 \dots t-24$) and rolling moving averages.
- **Horizon**: 12 hours ahead with 95% confidence bands.
- **Overall Performance**:
  - Electricity MAE: **6.21 kWh** | RMSE: **8.94 kWh**
  - Water MAE: **64.8 Litres** | RMSE: **92.3 Litres**

---

## 📝 Output Files Generated

| File Path | Description | Records |
| :--- | :--- | :--- |
| `outputs/data_inspection_report.txt` | Comprehensive schema, null value, duplicate, and relationship audit | 286 lines |
| `outputs/model_metrics.json` | Exact measured model validation metrics and confusion matrix | Full JSON |
| `outputs/waste_events_test_predictions.csv` | Exactly 1,601 predictions matching `waste_events_test.xlsx` | 1,601 rows |
| `outputs/anomaly_report.csv` | Detected off-hours, non-working day, and surge consumption anomalies | 7,277 rows |
| `outputs/recommendations.csv` | Prioritized maintenance actions with cost and CO2 impact | 300 rows |
| `outputs/forecast_results.csv` | 12-hour ahead electricity and water projections with bounds | 192 rows |

---

## ⚙️ Configurable Financial & Sustainability Assumptions

Configured transparently in `config.py`:
- **Electricity Tariff**: ₹8.00 per kWh
- **Grid Carbon Emission Factor**: 0.70 kg CO2 per kWh
- **Water Pumping Electricity Factor**: 0.85 kWh per 1,000 Litres (kL)
- **Savings Factor**: 65% of detected anomalous excessive consumption deemed avoidable.

## 🧭 Application Navigation & Feature Map

The platform is consolidated into 8 purpose-driven operational consoles adhering to **"LESS READING, MORE UNDERSTANDING"**:

1. **Overview**: Executive landing console tracking total electricity, water, solar generation, carbon footprint, and the **"What Needs Immediate Attention?"** critical alert feed.
2. **Resources**: Building-level deep-dive analytics, 24-hour rolling baselines, operating (08:00–18:00) vs off-hours (19:00–07:00) curves, and normalized intensities ($kWh/m^2$ and $L/m^2$).
3. **Forecasts**: Multi-hour forward projections (6–24 hours) for building electricity and water demand with solid historical curves, dashed predictions, 95% confidence bands, and CSV downloads.
4. **AI Lab**: Guided workflow with 4-step progress stepper (`01 · DATA` -> `02 · CONFIGURE` -> `03 · TRAIN & TEST` -> `04 · RESULTS`), task selection cards, compact dataset readiness panel, simple model parameters with advanced expander, dual-layer results (Beginner vs Technical view), dual-mode testing (Mode A Labeled vs Mode B Unlabeled with CSV export preserving `event_id` and row order), experiment comparison leaderboard, and model registry management.
5. **Alerts**: Prioritized anomaly feed answering *"What needs attention right now?"* with severity tags (`CRITICAL`, `HIGH`, `MEDIUM`), excess deviations, interactive filters, and field inspection checklists.
6. **Recommendations**: Direct, evidence-grounded maintenance directives structured around: `ISSUE` -> `EVIDENCE` -> `ACTION` -> `EXPECTED IMPACT`, with clear distinction between measured telemetry and estimated savings.
7. **Sustainability**: Comprehensive benchmarking and circularity hub combining the normalized building sustainability leaderboard ($kWh/m^2$, $L/m^2$, hygiene scores, improvement roadmaps) with smart-bin circular material recovery loops.
8. **System Health**: Infrastructure resilience console consolidating data completeness audits, SQLite persistence status, real-world failure mode defenses (sensor drift, concept drift, network loss), and reference methodology.

---

## 🧪 AI/ML Model Lab: 9-Step Guided Workflow Guide

The **AI/ML Model Lab** is an interactive studio designed for both beginners and technical engineers:

### Step 1: Choose a Task
Select from 4 distinct operational tasks:
- **Waste Classification**: Classify smart-bin sensor events into circular categories (`food_organic`, `plastic`, `paper_cardboard`, `metal`, `glass`, `ewaste`).
- **Energy Forecasting**: Project upcoming facility electricity demand.
- **Water Forecasting**: Anticipate upcoming bulk water demand.
- **Anomaly Detection**: Adjust statistical sensitivity to identify base-load leakage.

### Step 2: Select & Validate Dataset
- Choose existing campus datasets (`waste_events_train.xlsx`, `hourly_streams.xlsx`, etc.) or upload custom CSV/Excel files.
- Inspect the **Dataset Readiness Panel** (Row count, target validation, feature validity, missing values).

### Step 3: Configure Algorithm & Hyperparameters
- Select from **Random Forest**, **Decision Tree**, **Logistic Regression**, or **Gradient Boosting**.
- Adjust real parameters via UI widgets (trees, depth, split criteria, regularization $C$, class weights).
- Configure preprocessing: missing value imputer (`median`, `mean`, `most_frequent`) and numeric scaler (`StandardScaler`, `MinMaxScaler`, `None`).
- Set validation split slider (10% to 40%).

### Step 4: Train the Model
- Click **`🚀 TRAIN MODEL`** to fit the Scikit-Learn pipeline. Training execution time and validation metrics are measured and saved to `models/`.

### Step 5: Dual-Layer Results Explanation
- **Beginner View**: Plain-language summary explaining what the model predicted, overall reliability percentage, and practical next steps.
- **Technical View**: Exact numerical metrics, interactive Confusion Matrix heatmap, and full classification report.

### Step 6: Test Model (Mode A vs Mode B)
- **Mode A (Labeled Evaluation)**: Evaluates accuracy, precision, recall, macro-F1, confusion matrix, and multiclass ROC-AUC against known target labels.
- **Mode B (Unlabeled Inference)**: Predicts categories and confidence probabilities for unlabelled streams while strictly preserving original event IDs and row order.
- Download output predictions as CSV.

### Step 7: Compare Experiment Runs
- Inspect the experiment comparison leaderboard, compare validation Macro-F1 across runs via grouped bar charts, and highlight the champion configuration.

### Step 8: Feature Importance
- View horizontal bar charts ranking relative input signal weights.
- Includes statistical disclaimer distinguishing correlation from causation.

### Step 9: Model Lifecycle Management
- Inspect serialized `.joblib` files, view metadata, and delete deprecated models after explicit checkbox confirmation.

---

## 📚 Technical Metric Interpretation Guide

| Metric | Plain-Language Meaning | Better Direction | Real-World Campus Utility Interpretation |
| :--- | :--- | :---: | :--- |
| **Accuracy** | Fraction of total records predicted correctly. | Higher ↑ | Overall percentage of correctly classified waste events or operational states. |
| **Precision** | When the model predicts category $X$, how often is it actually $X$? | Higher ↑ | High precision ensures few false alarms (e.g. low false positive sorting into compost). |
| **Recall** | Of all actual instances of category $X$, how many did the model capture? | Higher ↑ | High recall ensures minimal missed recyclable materials. |
| **Macro-F1** | Balanced unweighted F1 average across all categories. | Higher ↑ | Primary benchmark: balances rare classes (e-waste) equally with frequent classes (food organic). |
| **MAE** | Mean Absolute Error: average magnitude of prediction error. | Lower ↓ | Numerical error in kilowatt-hours (kWh) or litres (L) from observed historical demand. |
| **RMSE** | Root Mean Squared Error: penalizes large deviation spikes heavily. | Lower ↓ | Evaluates accuracy during peak surge periods. |
| **Confusion Matrix** | Table comparing ground-truth targets vs model predictions. | Diagonal | Diagnoses cross-contamination patterns (e.g. mistaking cardboard for plastic). |

---

## ⚙️ Configurable Financial & Sustainability Assumptions

1. **Sub-Metering Granularity**: Telemetry is currently aggregated at the whole-building level; installing departmental sub-meters will enable room-level root cause tracing.
2. **Dynamic Tariffs**: Current financial models use fixed rates; integrating peak/off-peak Time-of-Day (ToD) tariffs will further refine monetary savings projections.
3. **Automated Actuation**: Direct Modbus/BACnet integration to automatically signal BMS HVAC setbacks upon persistent anomaly flags.
