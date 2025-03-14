import socket


def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} for open ports...\n")

    for port in range(start_port, end_port +1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            s.close()

target_ip = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

scan_ports(target_ip,start_port,end_port)