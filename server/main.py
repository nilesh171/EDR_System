from fastapi import FastAPI
from pymongo import MongoClient
from detection import analyze_process, classify_severity
from datetime import datetime

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client.edr


@app.get("/health")
def health():
    return {"status": "EDR Server Running"}


@app.post("/logs")
def ingest_logs(payload: dict):
    """
    Receives telemetry from Windows agents,
    stores raw logs, runs detection, and
    generates alerts if required.
    """

    db.telemetry.insert_one(payload)

    endpoint_id = payload.get("endpoint_id")
    processes = payload.get("processes", [])

    for process in processes:
        risk_score, evidence = analyze_process(process)
        severity = classify_severity(risk_score)

        if severity == "HIGH" or severity == "MEDIUM":
            alert = {
                "endpoint_id": endpoint_id,
                "alert_type": "Suspicious Process Execution",
                "severity": severity,
                "risk_score": risk_score,
                "evidence": evidence,
                "process": {
                    "pid": process.get("pid"),
                    "name": process.get("name"),
                    "exe": process.get("exe"),
                    "username": process.get("username")
                },
                "status": "OPEN",
                "created_at": datetime.utcnow()
            }

            db.alerts.insert_one(alert)

    return {"status": "processed"}
