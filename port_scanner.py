import socket
import threading
 

target=input("Enter the target IP address: ")
start_port=int(input("Enter the starting port number: "))
end_port=int(input("Enter the ending port number: "))
print(f"\nScanning target:{target} |PORTS: {start_port}-{end_port}\n")

SERVICES={
    21:"FTP", 22:"SSH",23:"TELNET",25:"SMTP",53:"DNS",
    80:"HTTP",110:"POP3",143:"IMAP",443:"HTTPS",3306:"MySQL",
    3389:"RDP",8080:"HTTP-Alt"
}

def grab_banner(s):
    try:
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner=s.recv(1024).decode("utf-8", errors="ignore").strip()
        return banner
    except:
        return None
def scan_port(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result=s.connect_ex((target, port))
    if result == 0:
        service=SERVICES.get(port,"Unknown")
        banner=grab_banner(s)
        if banner:
            print(f"Port {port} OPEN - {service}\n Banner: {banner[:100]}")
        else:
            print(f"Port {port} OPEN - {service}")
    s.close()

threads=[]
for port in range(start_port, end_port+1):
    t=threading.Thread(target=scan_port,args=(port,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("\nScan Completed.")
