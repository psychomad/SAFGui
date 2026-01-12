# SAFGui
real-time web interface for the Centuria SCADA Application Firewall.

Centuria SAF Dashboard
The Centuria SAF Dashboard is an optional, real-time web interface for the Centuria SCADA Application Firewall. It provides a visual overview of network traffic, security incidents, and active blacklists.

🛠️ Installation
The dashboard is built using Python 3.12 and Streamlit. Follow these steps to set up your environment:

1. Create a Virtual Environment (Recommended)
To avoid conflicts with system-wide Python packages:

Bash

python3 -m venv venv
source venv/bin/activate
2. Install Dependencies
Ensure you have the requirements.txt file in your directory, then run:

Bash

pip install -r requirements.txt
Dependencies: streamlit, pandas, requests, plotly.

🚀 How to Use
To successfully monitor your network, the SAF Core and the GUI must work together.

Step 1: Start the SAF Core (Rust)
Navigate to your Rust project folder and launch the firewall. Ensure the API server starts on port 3000.

Bash

cargo run
Step 2: Start the Dashboard
In a separate terminal, navigate to the GUI folder and run:

Bash

streamlit run safGUI.py
Step 3: Access the Interface
Once launched, Streamlit will provide a local URL (usually http://localhost:8501). Open this in your browser to see:

Total Packets: Real-time counter of processed industrial traffic.

Blocked Attacks: Live count of dropped packets (DPI failures or DDoS).

Active Blacklist: Number of IPs currently banned from the system.

Network Load Graph: A 2D line chart showing traffic trends.

⚙️ Configuration
API URL: By default, the GUI looks for the SAF API at http://localhost:3000. If you are running the SAF on a different machine, update the URL in the Sidebar of the web interface.

Dark Mode: The dashboard is hard-coded for Cyber-Dark Mode for maximum visibility in Control Room environments.

🔍 Troubleshooting
"Connection Offline": This means the GUI cannot reach the Rust SAF. Verify that the Rust program is running and that port 3000 is not blocked by a firewall.

"ScriptRunContext Missing": Always start the app using streamlit run safGUI.py, never with python3 safGUI.py.
