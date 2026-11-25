@echo off
chcp 65001 >nul
cd /d %~dp0
if not exist venv (
  echo Creating virtual environment...
  python -m venv venv
)
call venv\Scripts\activate
echo Installing requirements...
pip install -r requirements.txt
echo Starting ISO Advisor...
streamlit run app.py
pause
