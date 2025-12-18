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


- Banner Grabbing: 
Sends a lightweight probe to extract service banners
(e.g., Apache, SSH versions, SMTP greetings, etc.).

- Multi-Target Scanning: 
Supports scanning a single host or multiple hosts separated by commas.

- Colored Output: 
Open ports are highlighted using termcolor for readability.

- Execution Time Measurement: 
Displays the total running time of the scanning process.

   Requirements

  - Install dependencies:

    - pip install scapy
  
    - pip install termcolor


(Scapy may require administrator/root privileges to send ICMP packets on some systems).

   Usage:

  - Run the script:

    - python scanner.py


You will be prompted to enter:

Target(s):

- Enter targets (separated by commas):

Ports:

- Enter number of ports: 

----------------------------------------------------------------------------------

   Example:

- Enter targets: 192.168.1.10

- Enter number of ports: 100

[*] Scanning 192.168.1.10

[+] Open port 22  (SSH)

[+] Open port 80  (HTTP - Apache/2.4.41)

OS Detection: Likely Linux (TTL=64)

Scan completed in 2.41 seconds

----------------------------------------------------------------------------------

   Why This Project?

This tool was developed to demonstrate:

- Low-level networking knowledge

- Ability to combine Scapy with raw sockets

- Understanding of service fingerprinting

- Practical cybersecurity tool development

- Modular, extensible Python design

Its goal is to serve as part of a Cybersecurity + AI portfolio, showing foundational skills in threat analysis and network reconnaissance.

----------------------------------------------------------------------------------

Disclaimer:

This tool is intended strictly for educational and ethical security research.
Do NOT scan systems without explicit permission.
Unauthorized scanning may violate local laws and regulations.





