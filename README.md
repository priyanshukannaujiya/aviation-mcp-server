✈️ Aviation MCP Server – End-to-End Flight Delay Prediction & Explanation System

An end-to-end, production-style Data Engineering & ML system that predicts flight delays and explains WHY they occur, using MCP-style tool orchestration, a FastAPI backend service, and AWS EC2 cloud deployment.

This project demonstrates how to convert a notebook-level ML model into a real-world, always-on, explainable AI system.

🎯 Problem Statement

Traditional ML systems only answer:

“Will the flight be delayed?”

But real aviation systems require:

“WHY is the flight delayed?”

This project solves:

Prediction (ML)

Explanation (MCP tools)

Reliability (Backend service)

Availability (AWS EC2)

🚀 What I Built (A to Z)
✅ Data Engineering & ETL

Collected raw historical flight data

Cleaned missing values & duplicates

Feature engineering (time, weather, congestion)

Prepared ML-ready dataset

✅ Machine Learning

Trained delay prediction model

Evaluated performance

Saved trained model (model.pkl)

✅ MCP (Core Differentiator 🔥)

Used MCP as an intelligent tool orchestration layer, not just monitoring.

MCP Tools Created:

Prediction Tool (ML + business rules)

Weather Analysis Tool

Airport Congestion Tool

Historical Delay Pattern Tool

Flow:

ML predicts delay

MCP selects relevant tools

Tools analyze reasons

MCP generates human-readable explanation

⚙️ Backend Service (FastAPI)
Why Backend Service?

UI should not directly talk to ML logic

MCP tools need orchestration

Production systems need separation of concerns

What Backend Does

Loads ML model

Triggers MCP tools

Returns prediction + explanation

Acts as bridge: UI ↔ ML ↔ MCP

☁️ Why AWS EC2

Local laptop = unreliable

EC2 = 24/7 always-on server

Production-like cloud environment

Public access for real users

🌐 Why Elastic IP

EC2 public IP changes on restart

Elastic IP provides:

Fixed URL

Stable frontend-backend communication

Professional deployment

🧠 System Architecture
End User (Browser)
        ↓
Streamlit UI (Port 8501)
        ↓
FastAPI Backend Service (Port 8000)
        ↓
MCP Tool Orchestration
        ├── ML Prediction Tool
        ├── Weather Reasoning Tool
        ├── Congestion Reasoning Tool
        └── Historical Pattern Tool
        ↓
AWS EC2 (Elastic IP attached)

🛠️ Tech Stack

Python

Pandas / NumPy (ETL)

Scikit-learn\db (ML)

FastAPI (Backend MCP server)

Streamlit (Frontend UI)

AWS EC2 (Ubuntu)

Elastic IP

📂 Project Structure
aviation-mcp-server/
│
├── app.py                     # Streamlit UI
├── mcp_server.py              # FastAPI MCP backend
├── model.pkl                  # Trained ML model
├── requirements.txt
├── cleaned_flight_data.csv
│
├── notebooks/
│   └── 01_data_cleaning.ipynb
│
├── training/
│   └── model.py
│
└── README.md

▶️ Run Locally
git clone https://github.com/<your-username>/aviation-mcp-server.git
cd aviation-mcp-server

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn mcp_server:app --reload

streamlit run app.py

☁️ AWS EC2 DEPLOYMENT (INTERVIEW GOLD 🥇)
🔹 EC2 Setup

Ubuntu EC2 instance

Security Group ports:

22 → SSH

8000 → Backend

8501 → Streamlit

🔹 EC2 Commands Used
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y

git clone https://github.com/<your-username>/aviation-mcp-server.git
cd aviation-mcp-server

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🔥 Backend as SYSTEMD Service (IMPORTANT)
Create Service File
sudo nano /etc/systemd/system/mcp_backend.service

[Unit]
Description=MCP FastAPI Backend Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/aviation-mcp-server
ExecStart=/home/ubuntu/aviation-mcp-server/venv/bin/uvicorn mcp_server:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target

Enable & Start
sudo systemctl daemon-reload
sudo systemctl enable mcp_backend
sudo systemctl start mcp_backend
sudo systemctl status mcp_backend

🖥️ Run Streamlit in Background
nohup streamlit run app.py \
--server.port 8501 \
--server.address 0.0.0.0 &

🌐 Live Application (Deployed on AWS EC2)

Streamlit UI (Live & Public):
👉 http://13.62.216.124:8501/

Backend API Documentation (FastAPI – MCP Server):
👉 http://13.62.216.124:8000/docs

The application is deployed on an AWS EC2 instance with an attached Elastic IP to ensure a stable and permanent endpoint.

👤 Author

Priyanshu Kannaujiya


