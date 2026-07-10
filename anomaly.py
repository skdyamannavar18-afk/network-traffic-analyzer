import pandas as pd

df = pd.read_csv("capture_data.csv")

# Bucket packets into 1-second windows
df["time_bucket"] = df["time"].astype(int)

# Count packets per source IP per 1-second window
rate_table = df.groupby(["time_bucket", "src"]).size().reset_index(name="packet_count")

# Threshold: flag any IP sending more than THRESHOLD packets in a single second
THRESHOLD = 15

anomalies = rate_table[rate_table["packet_count"] > THRESHOLD]

print(f"Total packets analyzed: {len(df)}")
print(f"Threshold: more than {THRESHOLD} packets/sec from a single IP\n")

if anomalies.empty:
    print("No anomalies detected in this capture.")
else:
    print(f"{len(anomalies)} anomaly window(s) detected:\n")
    print(anomalies.to_string(index=False))

anomalies.to_csv("anomalies_detected.csv", index=False)