from scapy.all import sniff, IP

# Global variables for anomaly detection (adjust these thresholds as needed)
THRESHOLD_PACKET_SIZE = 100  # Example: Detect packets larger than 1500 bytes

def packet_handler(packet):
    if IP in packet:  # Check if the packet contains the IP layer
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto  # Protocol number (e.g., 6 for TCP, 17 for UDP)
        packet_size = len(packet)  # Get packet size
        
        # Check for anomaly: Packet size larger than the threshold
        if packet_size > THRESHOLD_PACKET_SIZE:
            print(f"Anomaly Detected! Source: {src_ip} -> Destination: {dst_ip} Protocol: {protocol} Packet Size: {packet_size}")

# Capture packets and perform anomaly detection (change the interface as needed)
sniff(iface="Wi-Fi", prn=packet_handler, count=10)
