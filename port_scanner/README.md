  Network Scanner & OS Fingerprinting Tool (Python + Scapy)


This project is a lightweight network scanner built in Python, designed to detect open ports, identify services, grab banners, and estimate the target operating system using ICMP TTL analysis.

It combines Scapy, socket programming, and basic fingerprinting techniques to provide quick reconnaissance capabilities.

Features

- Port Scanning

- Attempts TCP connections on a user-defined port range

- Reports open ports

- Displays detected service (based on port or banner)

- Shows captured banner when available

   

OS Detection

Uses ICMP Echo Reply TTL values to estimate the system type:

| Approx. TTL | Likely OS               |
| ----------- | ----------------------- |
| 64          | Linux/Unix              |
| 128         | Windows                 |
| 240+        | Cisco / network devices |


- Benner Grabbing: 
Sends a lightweight probe to extract service banners
(e.g., Apache, SSH versions, SMTP greetings, etc.).

- Multi-Target Scanning: 
Supports scanning a single host or multiple hosts separated by commas.

- Colored Output: 
Open ports are highlighted using termcolor for readability.

- Execution Time Measurement: 
Displays the total running time of the scanning process.

- Requirements

  - Install dependencies:

    - pip install scapy
  
    - pip install termcolor


Note: Scapy may require administrator/root privileges to send ICMP packets on some systems.

- Usage:

  - Run the script:

    - python scanner.py


You will be prompted to enter:

Target(s):
Enter targets (separated by commas):


Disclaimer:

This tool is intended strictly for educational and ethical security research.
Do NOT scan systems without explicit permission.
Unauthorized scanning may violate local laws and regulations.
