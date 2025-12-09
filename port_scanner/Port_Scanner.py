from scapy.all import *
import socket
import time
from termcolor import colored

start = time.time()

# Main scanning function
def scan(target, ports):
    print(f"Scanning IP {target}")
    host_name()
    detect_os(target)

    for port in range(1, ports + 1):
        scan_port(target, port)

# OS detection using ICMP TTL
def detect_os(target):
    ip = target
    response = sr1(IP(dst=ip)/ICMP(), timeout=2)

    if response is None:
        print("No response received")
    else:
        ttl = response.ttl
        print(f"TTL of response: {ttl}")

        if 60 <= ttl <= 70:
            print("Likely Linux system -- TTL ≈ 64")
        elif 120 <= ttl <= 130:
            print("Likely Windows system -- TTL ≈ 128")
        elif ttl >= 240:
            print("Likely Cisco device -- TTL ≈ 240")

# Port scanning and service fingerprinting
def scan_port(ipaddrs, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddrs, port))

        service, banner = fingerprint_service(ipaddrs, port)

        print(colored(f"[+] Open port: {port} | Service: {service} | Banner: {banner}", "green"))

        results.append({"port": port, "service": service, "banner": banner})

        sock.close()
        return True

    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

# Local hostname
def host_name():
    hostname = socket.gethostname()
    print("Local system: " + str(hostname))

# Basic banner grabbing
def fingerprint_service(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((ip, port))

        try:
            sock.send(b"Hello")
            banner = sock.recv(1024).decode(errors="ignore").strip()
        except:
            banner = None

        sock.close()

        service = identify_protocol(port, banner)
        return service, banner

    except (socket.timeout, ConnectionRefusedError, OSError):
        return "Unknown", None

# Identify service by port or banner
def identify_protocol(port, banner):

    known = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
    }

    if port in known:
        return known[port]

    if banner:
        b = banner.lower()
        if "ftp" in b:
            return "FTP"
        if "ssh" in b:
            return "SSH"
        if "smtp" in b:
            return "SMTP"
        if "http" in b:
            return "HTTP"

    return "Unknown"

results = []

targets = input("Enter targets (separated by commas): ")
ports = int(input("Enter number of ports to scan: "))

if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)

end = time.time()
print(f"Total time: {end - start:.2f} seconds")
