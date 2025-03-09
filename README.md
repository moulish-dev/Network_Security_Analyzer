# Network Security Analyzer (Windows-Compatible)

## Overview
The **Network Security Analyzer** is a tool designed to **capture network traffic**, **analyze packets**, and **detect vulnerabilities** using Nmap. It is compatible with Windows and leverages Python libraries like `scapy` and `python-nmap`.

## Features
- **Packet Sniffing**: Captures live network traffic and extracts essential details.
- **Port Scanning**: Uses Nmap to scan open ports and detect potential vulnerabilities.
- **Traffic Analysis**: Identifies communication between devices.
- **Windows Compatible**: Works with Windows using `Npcap` and `python-nmap`.

## Prerequisites
Make sure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Npcap (Packet Capture Driver)](https://npcap.com/#download)
- [Nmap (Network Scanner)](https://nmap.org/download.html)

## Installation
Run the following commands to install dependencies:
```bash
pip install scapy python-nmap pandas
```

### **Ensure Nmap is Added to Windows PATH**
1. Open **System Properties** → **Environment Variables**.
2. Under **System Variables**, select `Path` and click **Edit**.
3. Add: `C:\Program Files (x86)\Nmap\`
4. Verify Nmap installation:
   ```cmd
   nmap --version
   ```
   If it prints a version number, Nmap is correctly installed.

## Usage
### **1️. Capture Network Packets**
Run the following script to sniff packets on your network:
```python capture_packets.py
```
**Note:** Run the script **as Administrator** for packet sniffing to work on Windows.

### **2️. Scan Open Ports Using Nmap**
```python scan_network.py
```

### **3️. Run an Nmap Scan from CMD**
```cmd
nmap -sS -O -p 1-1000 192.168.1.1
```
- **`-sS`**: Stealth scan
- **`-O`**: Detect OS
- **`-p 1-1000`**: Scan first 1000 ports

## Disclaimer
This tool is for **educational purposes only**. Do not use it to scan networks you do not own or have explicit permission to test.

---
**Future Enhancements**
- Automated vulnerability detection
- Controlled attack simulations (using Metasploit or custom scripts)

