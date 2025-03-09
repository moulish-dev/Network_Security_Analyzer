import nmap

def scan_network(target):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target, arguments='-p 1-1000 -sV')

    for host in scanner.all_hosts():
        print(f"\nHost: {host} ({scanner[host].hostname()}) - {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(f"\nProtocol: {proto.upper()}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port: {port} | State: {scanner[host][proto][port]['state']}")

scan_network("192.168.1.1")  # Replace with your local network IP
