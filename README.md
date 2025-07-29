# Port Scanner

A simple and efficient Python script to scan open TCP ports on a specified target IP within a given port range.

## Features

- Scans a target IP for open TCP ports within a user-defined range.
- Displays open ports in real time.
- Handles connection timeouts and errors gracefully.
- User-friendly interactive command-line interface.

## Requirements

- Python 3.x

No external libraries are required; the script uses standard Python modules (`socket`, `time`).

## Usage

1. **Clone this repository:**

    ```bash
    git clone https://github.com/KeRoM-01/Port-Scanner.git
    cd Port-Scanner
    ```

2. **Run the script:**

    ```bash
    python "Port Scanner Script.py"
    ```

3. **Follow the prompts:**
    - Enter the target IP address (e.g., `192.168.1.1` or `localhost`).
    - Enter the start port (e.g., `1`).
    - Enter the end port (e.g., `1024`).

The script will scan each port in the specified range and display open ports as it finds them.

## Example Output

```
Enter target IP: 127.0.0.1
Enter start port: 75
Enter end port: 85

Scanning target: 127.0.0.1
Time started: 2025-07-29 11:04:24
--------------------------------------------------
[+] Port 80 is OPEN
--------------------------------------------------
Scan finished. Open ports: [80]
```

## Notes

- Use this script responsibly. Unauthorized port scanning may violate network policies or laws.
- Scanning a large port range may take some time depending on network latency and the target's responsiveness.

## License

This project is licensed under the MIT License.
