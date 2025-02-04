from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto, "Other")

        print(f"Source IP: {src_ip} → Destination IP: {dst_ip} | Protocol: {protocol_name}")

        if TCP in packet or UDP in packet:
            payload = bytes(packet[TCP].payload) if TCP in packet else bytes(packet[UDP].payload)
            if payload:
                print(f"Payload: {payload[:50]}")  # Display first 50 bytes of payload

# Capture packets (requires root/admin privileges)
print("Starting packet sniffing... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
