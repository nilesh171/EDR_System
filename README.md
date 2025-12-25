# 🛡️ Windows Mini EDR (Endpoint Detection & Response)

A **Windows-based Endpoint Detection & Response (EDR) system** that monitors real-time process activity, performs **behavior-based threat detection**, and generates **SOC-ready alerts** using a centralized backend.

> 🎯 Inspired by modern EDR platforms where **lightweight agents run on endpoints** and **detection logic lives centrally**.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Why This Project](#-why-this-project)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Detection Logic](#-detection-logic)
- [Installation & Setup](#-installation--setup)
- [Running the Project](#-running-the-project)
- [Viewing Telemetry & Alerts](#-viewing-telemetry--alerts)
- [Safe Testing](#-safe-testing)
- [SOC Workflow](#-soc-workflow)
- [Security Design Decisions](#-security-design-decisions)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Resume Summary](#-resume-summary)

---

## 🔍 Overview

This project implements a **mini yet realistic EDR system for Windows** that focuses on **visibility, detection, and explainability** rather than aggressive auto-remediation.

The system consists of:
- 🖥️ A **Windows endpoint agent** for telemetry collection  
- ☁️ A **centralized FastAPI server** for ingestion and detection  
- 🧠 A **rule-based detection engine** with risk scoring  
- 🚨 A **SOC-style alert pipeline** stored in MongoDB  

---

## ❓ Why This Project

Traditional antivirus relies on **signatures** and often fails against:
- Zero-day malware  
- Living-off-the-land attacks  
- Fileless techniques  

This project demonstrates how **modern EDR systems detect threats based on behavior**, not signatures.

---

## ✨ Key Features

- ✅ Real-time Windows process monitoring  
- ✅ Centralized telemetry ingestion via REST API  
- ✅ Behavior-based threat detection  
- ✅ Weighted risk scoring & severity classification  
- ✅ Explainable alerts (clear evidence for SOC analysts)  
- ✅ Safe-by-design (no automatic killing of processes)  

---


**Design Principle:**  
> *Endpoints collect data → Server analyzes → Humans decide*

---

## 🧰 Tech Stack

| Layer | Technology |
|----|----|
| Endpoint Agent | Python, psutil |
| Backend API | FastAPI |
| Detection Engine | Python (rule-based) |
| Database | MongoDB |
| Operating System | Windows |
| Version Control | Git & GitHub |

---



---

## ⚙️ How It Works

1. 🖥️ The agent runs continuously on a Windows endpoint  
2. 📊 It collects process telemetry (PID, path, user, CPU, memory)  
3. ☁️ Telemetry is sent to the central server  
4. 🧠 Detection engine evaluates behavioral indicators  
5. 🚨 High-risk activity generates alerts  
6. 🧑‍💻 SOC analyst reviews alerts and timelines  

---

## 🧠 Detection Logic

This EDR uses **behavior-based detection**, not malware signatures.

### 🔎 Behavioral Indicators
- Execution from `Temp` directories  
- Administrator / SYSTEM privilege usage  
- Sustained high CPU usage (e.g., crypto-mining behavior)  

### ⚖️ Risk Scoring

Each indicator contributes to a weighted score.

| Risk Score | Severity |
|----|----|
| < 0.3 | LOW |
| 0.3 – 0.6 | MEDIUM |
| > 0.6 | HIGH |

Alerts include **evidence**, making them explainable and SOC-friendly.

---

## 🛠️ Installation & Setup

### 1️⃣ Prerequisites
- Python 3.9+
- MongoDB (local or MongoDB Atlas)
- Git

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

## 🚀 Future Improvements

Planned enhancements to evolve this project toward a full enterprise-grade EDR platform:

- 🔍 **Parent–child process correlation**  
  Detect suspicious execution chains by analyzing relationships between parent and child processes.

- 🌐 **Network telemetry collection**  
  Monitor outbound/inbound connections to identify data exfiltration, command-and-control traffic, and lateral movement.

- 📊 **Web-based dashboard (React)**  
  Build an interactive SOC dashboard for real-time visibility into endpoints, alerts, timelines, and investigation workflows.

- 📧 **SMTP-based direct alert notifications**  
  Integrate SMTP email alerts to notify SOC analysts instantly when high-severity threats are detected, enabling faster response.

- 🤖 **ML-based anomaly detection**  
  Apply machine learning models to identify abnormal behavior patterns beyond rule-based detection.

- ☁️ **Secure cloud deployment**  
  Deploy the EDR backend on the cloud using HTTPS, authentication tokens, and role-based access control for secure multi-endpoint monitoring.

