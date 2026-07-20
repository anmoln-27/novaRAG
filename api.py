from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import json
import os
import subprocess

app = FastAPI(title="novaRAG Backend API")

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REPORT_PATH = "reports/security_report.json"
HISTORY_PATH = "reports/history.json"
STRATEGY_PATH = "reports/strategy.json"


@app.get("/")
def home():
    return {
        "message": "novaRAG Backend Running"
    }


# -------------------------------------------------
# Get Final Security Report
# -------------------------------------------------
@app.get("/api/report")
def get_report():

    if not os.path.exists(REPORT_PATH):
        return {
            "error": "No report generated yet."
        }

    with open(REPORT_PATH, "r") as file:
        return json.load(file)


# -------------------------------------------------
# Get Attack History
# -------------------------------------------------
@app.get("/api/history")
def get_history():

    if not os.path.exists(HISTORY_PATH):
        return []

    with open(HISTORY_PATH, "r") as file:
        return json.load(file)


# -------------------------------------------------
# Get Attack Strategy
# -------------------------------------------------
@app.get("/api/strategy")
def get_strategy():

    if not os.path.exists(STRATEGY_PATH):
        return {}

    with open(STRATEGY_PATH, "r") as file:
        return json.load(file)


# -------------------------------------------------
# Run New Scan
# -------------------------------------------------
@app.post("/api/run")
def run_scan():

    subprocess.run(["python", "main.py"])

    if os.path.exists(REPORT_PATH):

        with open(REPORT_PATH, "r") as file:
            return json.load(file)

    return {
        "status": "Scan completed"
    }