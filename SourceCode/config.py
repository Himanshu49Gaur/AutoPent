import os

# Metasploit RPC Configuration
METASPLOIT_RPC_HOST = os.getenv("METASPLOIT_RPC_HOST" )
METASPLOIT_RPC_PORT = int(os.getenv("METASPLOIT_RPC_PORT" ))
METASPLOIT_RPC_PASS = os.getenv("METASPLOIT_RPC_PASS" )

# Attack Machine Details
LHOST = os.getenv("LHOST")
LPORT = int(os.getenv("LPORT"))  # Reverse shell listener port

# API Keys for Reconnaissance
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
BINARYEDGE_API_KEY = os.getenv("BINARYEDGE_API_KEY")
ONYPHE_API_KEY = os.getenv("ONYPHE_API_KEY")

# File Paths for Privilege Escalation Scripts
LINPEAS_PATH = os.getenv("LINPEAS_PATH", "/app/scripts/linpeas.sh")
WINPEAS_PATH = os.getenv("WINPEAS_PATH", "/app/scripts/winPEASany.exe")

# AI Model Path (LLaMA)
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH")

# Haiku API Configuration
HAIKU_API_KEY = os.getenv("HAIKU_API_KEY")
HAIKU_API_URL = os.getenv("HAIKU_API_URL")

print("all is working")
