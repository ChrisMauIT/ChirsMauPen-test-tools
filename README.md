# ChirsMauPen-test-tools
Custom tools for offensive security, penetration testing, and red teaming
#  Offensive Security Toolkit

This repo contains custom tools and scripts designed for use in real-world penetration testing, red teaming, and cloud security assessments. Built with speed and adaptability in mind.

---

## 🧰 Tools

### 🔍 Nessus Parser
- `parse_nessus.py`: Parses Nessus CSV output, filters high-priority vulnerabilities by CVSS or plugin family.
- **Use case**: Prioritization and triage in MSSP environments.

```bash
python3 parse_nessus.py nessus_export.csv

### 🌐 Burp Suite JSON Parser
- `parse_burp_json.py`: Extracts critical/high web app issues from Burp Suite’s JSON export.
- **Use case**: Streamlines manual scan review, useful for integration into ticketing pipelines.
bash
python3 parse_burp_json.py burp_output.json


### 🏛️ Active Directory & GPO Audit
- `ad_enum_audit.ps1`: Enumerates domain admins, checks GPO permissions, SPNs, and user password flags.
- **Use case**: Fast AD review for privilege escalation and misconfig identification.

Powershell
.\ad_enum_audit.ps1


### 🎣 Phishing Payload Server
- `app.py`: Flask app that generates and serves phishing payloads dynamically.
- **Use case**: Used in phishing simulations and red team C2 payload delivery.

bash

python3 app.py
# Then visit: http://localhost:8000/payload/xyz


### 🧱 Lateral Movement Toolkit
- `lateral_movement_toolkit.ps1`: Automates lateral movement via PsExec and WMI after gaining creds.
- **Use case**: Red team toolkit for internal movement post-initial access.

Powershell
.\lateral_movement_toolkit.ps1
# Requires a file called targets.txt with hostnames

### ☁️ Cloud Enumeration Script
- `aws_gcp_enum.sh`: Enumerates IAM roles, policies, buckets, and misconfigs in AWS and GCP.
- **Use case**: Quick cloud recon and privilege escalation discovery.

bash 
bash aws_gcp_enum.sh

---

## 🔒 Disclaimer
These scripts are for authorized security testing and educational purposes only.

---

### 👋 Hi, I'm [Your Name] — Penetration Tester & Security Consultant

🔐 I specialize in offensive security, red/purple teaming, and developing tools that reduce noise and boost impact.

- 🎯 Lead Penetration Testing engagements across enterprise networks, cloud, and applications
- 🧰 Builder of custom automation tools for security testing and reporting
- 🧠 Passionate about turning research into real-world offensive capabilities


