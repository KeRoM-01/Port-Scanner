import socket
import time

def port_scanner(target_ip, start_port, end_port):
    print(f"\nScanning target: {target_ip}")
    print("Time started:", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Timeout to skip unresponsive ports

            # Attempt to connect to the port
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            sock.close()

        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            exit()
        except socket.error:
            print(f"Error scanning port {port}")

    print("-" * 50)
    print("Scan finished. Open ports:", open_ports)

if __name__ == "__main__":
    # Replace with your target IP (e.g., "192.168.1.1" or "localhost")
    target_ip = input("Enter target IP: ")  
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    port_scanner(target_ip, start_port, end_port)