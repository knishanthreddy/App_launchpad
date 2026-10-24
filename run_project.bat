@echo off
setlocal EnableDelayedExpansion

set "ARG=%~1"
if not "%ARG%"=="" goto RUN_ARG

echo ============================================================================
echo Starting Predictive Circular-Resource Grid (PCRG)...
echo ============================================================================
echo Select an option:
echo [1] Launch Streamlit Interactive Dashboard
echo [2] Execute Full Pipeline (Retrain ML models, run forecasts, detect anomalies)
echo [3] Run Data Inspection Report
echo [4] Run Automated Test Suite
set /p USER_CHOICE="Enter choice [1-4] (default 1): "
if "%USER_CHOICE%"=="" set "USER_CHOICE=1"
set "ARG=%USER_CHOICE%"

:RUN_ARG
if "%ARG%"=="2" goto RUN_PIPELINE
if /i "%ARG%"=="pipeline" goto RUN_PIPELINE
if "%ARG%"=="3" goto RUN_INSPECT
if /i "%ARG%"=="inspect" goto RUN_INSPECT
if "%ARG%"=="4" goto RUN_TEST
if /i "%ARG%"=="test" goto RUN_TEST

:RUN_DASHBOARD
echo Launching Streamlit Interactive Dashboard...
streamlit run app.py
goto :EOF

:RUN_PIPELINE
echo Executing full pipeline (Retraining ML models, forecasting, anomalies, recommendations)...
python scripts\train_models.py
echo Pipeline execution complete.
goto :EOF

:RUN_INSPECT
echo Running data inspection...
python scripts\inspect_data.py
echo Inspection complete. See outputs\data_inspection_report.txt.
goto :EOF

:RUN_TEST
echo Running unit tests...
python tests\test_pipeline.py
goto :EOF
