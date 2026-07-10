from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time

captured = []
start_time = time.time()

def handle_packet(pkt):
    if IP in pkt:
        proto = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "OTHER"
        captured.append({
            "time": round(time.time() - start_time, 2),
            "src": pkt[IP].src,
            "dst": pkt[IP].dst,
            "proto": proto,
            "size": len(pkt),
        })

print("Capturing for 60 seconds...")
sniff(prn=handle_packet, timeout=60)

df = pd.DataFrame(captured)
df.to_csv("capture_data.csv", index=False)
print(f"Captured {len(df)} packets. Saved to capture_data.csv")
print(df.head())