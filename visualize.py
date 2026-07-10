import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("capture_data.csv")

# 1. Protocol distribution
proto_counts = df["proto"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(proto_counts, labels=proto_counts.index, autopct="%1.1f%%")
plt.title("Protocol Distribution")
plt.savefig("protocol_distribution.png")
plt.close()

# 2. Top talkers (by source IP)
top_talkers = df["src"].value_counts().head(5)
plt.figure(figsize=(8, 5))
top_talkers.plot(kind="bar", color="#1F3864")
plt.title("Top 5 Source IPs by Packet Count")
plt.ylabel("Packet Count")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("top_talkers.png")
plt.close()

print("Saved protocol_distribution.png and top_talkers.png")