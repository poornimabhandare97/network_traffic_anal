<h1>Network Traffic Anomaly Detection using Scapy</h1>

<p>This Python script uses the Scapy library to capture network packets and detect anomalies based on predefined thresholds. Anomalies are identified by packet size exceeding a specified threshold.</p>

<h2>Usage</h2>

<p><strong>Requirements:</strong></p>
<ul>
  <li>Python 3.x</li>
  <li>Scapy library (<code>pip install scapy</code>)</li>
</ul>

<p><strong>Run the Script:</strong></p>
<ol>
  <li>Update the <code>THRESHOLD_PACKET_SIZE</code> variable in the script to set the packet size threshold for anomaly detection.</li>
  <li>Execute the script using Python: <code>python scap.py</code></li>
</ol>

<h2>Description</h2>

<p>The script captures network packets using Scapy and checks each packet's size against the specified threshold. If a packet size exceeds the threshold, it triggers an anomaly detection message, indicating the source and destination IP addresses, protocol, and packet size.</p>

<h2>Customization</h2>

<ul>
  <li>Adjust the <code>THRESHOLD_PACKET_SIZE</code> variable to set the packet size threshold for anomaly detection according to your network's normal behavior.</li>
  <li>Modify the network interface (<code>iface</code>) in the <code>sniff</code> function to monitor a specific network interface.</li>
</ul>

<h2>Note</h2>

<p>Anomalies are determined based on predefined thresholds. Infrequent occurrences might not necessarily indicate issues but should be investigated in context. Further fine-tuning of anomaly detection may be necessary based on your network's specific characteristics and behavior.</p>

<h2>Disclaimer</h2>

<p>This script provides basic anomaly detection based on packet size thresholds. It might require further refinement and analysis to suit specific network environments.</p>
