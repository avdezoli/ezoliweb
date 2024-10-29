import socket
from datetime import datetime
import sys

def port_scanner(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}")
    open_ports = []

    # Başlangıç zamanı
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                
                if result == 0:
                    print(f"Port {port} is open")
                    open_ports.append(port)
                else:
                    print(f"Port {port} is closed")
                    
    except KeyboardInterrupt:
        print("Scan interrupted.")
        return
    
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return
    
    except socket.error:
        print("Could not connect to server.")
        return

    end_time = datetime.now()
    duration = end_time - start_time

    print("\nScan completed!")
    print(f"Open ports: {open_ports}")
    print(f"Time taken: {duration}")

if __name__ == "__main__" :
    ip_address = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    port_scanner(ip_address, start_port, end_port)

