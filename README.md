# Python Port Scanner

A multithreaded TCP port scanner built using Python.  
This tool scans a target IP or domain and identifies open ports along with basic service detection and banner grabbing.

# Features

- Multi-threaded port scanning
- TCP connect scan
- Service detection using common port mapping
- Basic banner grabbing
- Supports IP addresses and domain names

# Concepts Used

- Python sockets
- TCP/IP networking
- Threading
- DNS resolution

# How It Works

1. Takes target (IP/domain) and port range
2. Creates a thread for each port
3. Attempts TCP connection using sockets
4. Identifies open ports
5. Attempts to grab service banner

# sample output(Note: This was a controlled test of the script on a public testing server (scanme.nmap.org) to demonstrate its functionality and banner-grabbing capabilities.):
Enter the target IP address: scanme.nmap.org
Enter the starting port number: 20
Enter the ending port number: 100

Scanning target: scanme.nmap.org | PORTS: 20-100

Port 80 OPEN - HTTP
Banner: HTTP/1.1 200 OK
Date: Thu, 26 Mar 2026 07:22:07 GMT
Server: Apache/2.4.7 (Ubuntu)
Accept-Ranges:
Port 22 OPEN - SSH
Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13

Scan Completed.


