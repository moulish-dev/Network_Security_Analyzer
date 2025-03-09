from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        print(f"Packet: {packet[IP].src} -> {packet[IP].dst} | Protocol: {packet[IP].proto}")
    if TCP in packet or UDP in packet:
        print(f"Port: {packet.sport} -> {packet.dport}")

print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0, count=10)  # Capture 10 packets
