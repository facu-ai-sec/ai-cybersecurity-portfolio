from scapy.all import *
import socket
import time

start = time.time()

def scan(target, ports):
    print(f"Escaneando la IP {target}")
    host_name()
    system(target)

    for port in range(1, ports + 1):
        scan_port(target, port)


def system(target):
    ip = target
    respuesta = sr1(IP(dst=ip)/ICMP(), timeout=2)

    if respuesta is None:
        print("No hay respuesta")
    else:
        ttl = respuesta.ttl
        print(f"El ttl de la respuesta es: {ttl}")

        if 60 <= ttl <= 70:
            print("Sistema Linux -- TTL ≈ 64")
        elif 120 <= ttl <= 130:
            print("Sistema Windows -- TTL ≈ 128")
        elif ttl >= 240:
            print("Sistema Cisco -- TTL ≈ 240")


def scan_port(ipaddrs, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddrs, port))

        service, banner = fingerprint_service(ipaddrs, port)

        from termcolor import colored
        print(colored(f"[+] Puerto abierto: {port} | Servicio: {service} | Banner: {banner}", "green"))

        results.append({"port": port, "service": service, "banner": banner})

        sock.close()
        return True

    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def host_name():
    hostname = socket.gethostname()
    print("Sistema local: " + str(hostname))


def fingerprint_service(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((ip, port))

        try:
            sock.send(b"Hola")
            banner = sock.recv(1024).decode(errors="ignore").strip()
        except:
            banner = None

        sock.close()

        service = identify_protocol(port, banner)
        return service, banner

    except (socket.timeout, ConnectionRefusedError, OSError):
        return "Unknown", None


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
        banner_lower = banner.lower()
        if "ftp" in banner_lower:
            return "FTP"
        if "ssh" in banner_lower:
            return "SSH"
        if "smtp" in banner_lower:
            return "SMTP"
        if "http" in banner_lower:
            return "HTTP"

    return "Unknown"


results = []

targets = input("Escribí los objetivos (separados por ,): ")
ports = int(input("Escribí la cantidad de puertos a escanear: "))

if ',' in targets:
    print("[*] Escaneando múltiples objetivos")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)

end = time.time()
print(f"Tiempo total: {end - start:.2f} segundos")
