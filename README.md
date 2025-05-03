# 🛡️ CyberDefend Firewall Simulator

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.3.x-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based interactive firewall and intrusion detection system (IDS) simulator with real-time traffic monitoring, attack simulation, and rule management.

![Firewall UI Demo](https://via.placeholder.com/800x400?text=CyberDefend+UI+Demo) *(Replace with actual screenshot)*

## 🌟 Features

- **Firewall Rule Management**:
  - Add/delete allow/block rules via web interface
  - Persistent rule storage (JSON)
- **Attack Simulation**:
  - SYN flood attacks
  - Port scanning (simulated)
- **Traffic Monitoring**:
  - Real-time packet sniffing
  - Logging with timestamps
- **Educational UI**:
  - Bootstrap-powered dashboard
  - Interactive traffic visualization

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Windows 10/11 (for pydivert) or Linux (for scapy)
- Administrator privileges (for packet capture)

### Installation
```bash
# Clone the repository
git clone https://github.com/fidhathasnin/CyberDefend-FirewallSimulator.git
cd CyberDefend-FirewallSimulator

# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
