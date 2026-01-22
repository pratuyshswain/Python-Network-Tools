import socket
from datetime import datetime


def scan_ports(target_ip, start_port, end_port):
    print(f"Starting scan on host: {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Wait 1 sec before dropping

            # connect_ex returns 0 if connection is successful
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program.")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nServer not responding.")

    print("-" * 50)
    print("Scan completed.")

# Usage: Scan localhost (127.0.0.1) ports 20 to 80
scan_ports("127.0.0.1", 20, 80)