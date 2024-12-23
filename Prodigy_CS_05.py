from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    """Callback function to process each captured packet."""
    try:
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {packet[IP].proto}", end="")
            
            # Check for specific protocols
            if TCP in packet:
                print(", Protocol: TCP")
            elif UDP in packet:
                print(", Protocol: UDP")
            elif ICMP in packet:
                print(", Protocol: ICMP")
            else:
                print(", Protocol: Other")
            print("-" * 50)
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    print("Packet Sniffer Tool (Layer 3)")
    print("Capturing packets... Press Ctrl+C to stop.")
    try:
        # Sniff packets at Layer 3 (IP level)
        sniff(filter="ip", prn=packet_callback, store=False)
    except PermissionError:
        print("Permission denied! Run the script with elevated privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
