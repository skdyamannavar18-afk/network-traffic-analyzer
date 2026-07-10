from scapy.all import sniff, IP

def show_packet(pkt):
    if IP in pkt:
        print(f"{pkt[IP].src} -> {pkt[IP].dst}  proto={pkt[IP].proto}  size={len(pkt)}")

print("Sniffing for 15 seconds... browse something in another tab.")
sniff(prn=show_packet, timeout=15)