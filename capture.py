from scapy.all import sniff, IP, TCP, UDP
import pandas as pd

captured = []

def handle_packet(pkt):
    if IP in pkt:
        proto = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "OTHER"
        captured.append({
            "src": pkt[IP].src,
            "dst": pkt[IP].dst,
            "proto": proto,
            "size": len(pkt),
        })

print("Capturing 200 packets or 60 seconds, whichever comes first...")
sniff(prn=handle_packet, count=200, timeout=60)

df = pd.DataFrame(captured)
df.to_csv("capture_data.csv", index=False)
print(f"Captured {len(df)} packets. Saved to capture_data.csv")
print(df.head())