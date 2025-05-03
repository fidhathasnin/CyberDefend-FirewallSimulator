from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# File paths
RULES_FILE = "firewall_rules.json"
LOG_FILE = "traffic_logs.txt"

# Initialize files
if not os.path.exists(RULES_FILE):
    with open(RULES_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

def load_rules():
    with open(RULES_FILE, "r") as f:
        return json.load(f)

def save_rules(rules):
    with open(RULES_FILE, "w") as f:
        json.dump(rules, f)

def log_event(event):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {event}\n")

@app.route("/")
def index():
    return render_template("index.html", rules=load_rules())

@app.route("/add_rule", methods=["POST"])
def add_rule():
    ip = request.form.get("ip")
    action = request.form.get("action", "BLOCK")
    
    if not ip:
        flash("IP address is required", "danger")
        return redirect(url_for("index"))
    
    rules = load_rules()
    rules.append({"ip": ip, "action": action})
    save_rules(rules)
    
    log_event(f"Rule added: {action} {ip}")
    flash(f"Successfully added rule: {action} {ip}", "success")
    return redirect(url_for("index"))

@app.route("/delete_rule/<ip>")
def delete_rule(ip):
    rules = load_rules()
    updated_rules = [r for r in rules if r["ip"] != ip]
    
    if len(updated_rules) < len(rules):
        save_rules(updated_rules)
        log_event(f"Rule deleted: {ip}")
        flash(f"Deleted rule for {ip}", "success")
    else:
        flash("Rule not found", "warning")
    
    return redirect(url_for("index"))

@app.route("/logs")
def view_logs():
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()
    return render_template("logs.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")