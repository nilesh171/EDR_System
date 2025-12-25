def analyze_process(process):
    """
    Analyzes a single process and returns
    risk score and evidence list.
    """

    risk_score = 0.0
    evidence = []

    exe = (process.get("exe") or "").lower()
    user = (process.get("username") or "").lower()
    cpu = process.get("cpu_percent") or 0

    # Rule 1: Execution from Temp directory
    if "temp" in exe:
        risk_score += 0.4
        evidence.append("TEMP_EXECUTION")

    # Rule 2: Administrator / SYSTEM execution
    if "admin" in user or "system" in user:
        risk_score += 0.4
        evidence.append("ADMIN_PRIVILEGE")

    # Rule 3: High CPU usage (crypto-mining / abuse)
    if cpu > 60:
        risk_score += 0.2
        evidence.append("HIGH_CPU_USAGE")

    return risk_score, evidence


def classify_severity(risk_score):
    if risk_score > 0.7:
        return "HIGH"
    elif risk_score > 0.3:
        return "MEDIUM"
    else:
        return "LOW"
