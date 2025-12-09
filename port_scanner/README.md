Network Scanner \& OS Fingerprinting Tool (Python + Scapy)



This project is a lightweight network scanner built in Python, designed to detect open ports, identify services, grab banners, and estimate the target operating system using ICMP TTL analysis.

It combines Scapy, socket programming, and basic fingerprinting techniques to provide quick reconnaissance capabilities.



Features

Port Scanning



Attempts TCP connections on a user-defined port range



Reports open ports



Displays detected service (based on port or banner)



Shows captured banner when available



OS Detection



Uses ICMP Echo Reply TTL values to estimate the system type:



Approx. TTL	Likely OS

64	Linux/Unix

128	Windows

240+	Cisco / network devices

Banner Grabbing



Sends a lightweight probe to extract service banners

(e.g., Apache, SSH versions, SMTP greetings, etc.).



Multi-Target Scanning



Supports scanning a single host or multiple hosts separated by commas.



Colored Output



Open ports are highlighted using termcolor for readability.



Execution Time Measurement



Displays the total running time of the scanning process.



Requirements



Install dependencies:



pip install scapy

pip install termcolor





Note: Scapy may require administrator/root privileges to send ICMP packets on some systems.



Usage



Run the script:



python scanner.py





You will be prompted to enter:



Target(s):



Enter targets (separated by commas):





Examples:



192.168.1.10



192.168.1.10, 192.168.1.20



Number of ports to scan:



Enter number of ports to scan:





Example: 100 scans ports 1–100.



Output Example

Scanning IP 192.168.1.10

Local system: DESKTOP-1234

TTL of response: 128

Likely Windows system -- TTL ≈ 128

\[+] Open port: 22 | Service: SSH | Banner: SSH-2.0-OpenSSH\_8.2

\[+] Open port: 80 | Service: HTTP | Banner: Apache/2.4.41 (Ubuntu)

Total time: 3.52 seconds



File Structure

scanner.py        # Main scanning script

README.md         # Documentation



Disclaimer



This tool is intended strictly for educational and ethical security research.

Do NOT scan systems without explicit permission.

Unauthorized scanning may violate local laws and regulations.

