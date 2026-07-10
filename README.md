\# Network Traffic Analyzer



A Python tool that captures live network traffic using Scapy, parses it into a structured dataset, and visualizes protocol distribution and top talkers.



\## Features

\- Live packet capture (IP, protocol, size) using Scapy

\- Structured dataset export to CSV via pandas

\- Visualizations: protocol distribution (pie chart), top 5 source IPs by packet count (bar chart)



\## Tech Stack

Python, Scapy, Pandas, Matplotlib, Npcap (Windows packet capture driver)



\## How to Run

1\. Install Npcap (Windows) - https://npcap.com/

2\. `pip install scapy matplotlib pandas`

3\. Run as Administrator: `python capture.py` to capture traffic

4\. Run `python visualize.py` to generate charts



\## Note

Only run this on networks you own or have permission to monitor.



\## Sample Output

!\[Protocol Distribution](protocol\_distribution.png)

!\[Top Talkers](top\_talkers.png)

