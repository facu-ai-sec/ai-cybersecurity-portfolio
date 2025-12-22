# Network Scanner & OS Fingerprinting Tool  

---

## Overview

Lightweight network scanner written in Python, designed for fast and effective reconnaissance tasks.  
The tool allows you to identify exposed services and infer the target operating system using basic fingerprinting techniques.

**Capabilities include:**
- Detection of open TCP ports  
- Service identification  
- Banner grabbing  
- Operating system estimation via ICMP TTL analysis  

The project combines **Scapy**, low-level socket programming, and simple fingerprinting logic.

---

## Features

### Port Scanning
- Attempts TCP connections over a user-defined port range  
- Reports open ports  
- Identifies services based on port numbers or banners  
- Displays captured banners when available  

### OS Detection
Estimates the operating system using ICMP Echo Reply TTL values:

| Approx. TTL | Likely OS               |
|-------------|-------------------------|
| 64          | Linux / Unix            |
| 128         | Windows                 |
| 240+        | Cisco / Network Devices |

### Banner Grabbing
- Sends lightweight probes to retrieve service banners  
- Typical results include:
  - Apache versions  
  - SSH versions  
  - SMTP greetings  

### Multi-Target Scanning
- Supports scanning:
  - A single host  
  - Multiple hosts separated by commas  

### Colored Output
- Open ports are highlighted using `termcolor` for improved readability  

### Execution Time Measurement
- Displays the total runtime of the scan  

---

## Requirements

### Install Dependencies
```bash
pip install scapy
pip install termcolor
```
## Usage
- Run the Script

```bash
python scanner.py
```

Input Prompts

You will be asked to provide:

Target(s): one or more hosts (comma-separated)

Ports: number of ports to scan

## Example: 

- Enter targets: 192.168.1.10

- Enter number of ports: 100

- [*] Scanning 192.168.1.10

- [+] Open port 22 (SSH)

- [+] Open port 80 (HTTP - Apache/2.4.41)

- OS Detection: Likely Linux (TTL=64)

- Scan completed in 2.41 seconds

### Disclaimer

This tool is intended strictly for educational and ethical security research.
Do not scan systems without explicit authorization. Unauthorized scanning may violate local laws and regulations.

