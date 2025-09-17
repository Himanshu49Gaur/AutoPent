# AutoPent – Automated Penetration Testing Framework

## Overview

**AutoPent** is a **one of its kind, AI-powered penetration testing framework** designed to automate the complete security testing lifecycle.
It combines **reconnaissance, vulnerability scanning, exploitation, privilege escalation, AI-driven analysis, and automated reporting** into a single integrated platform.

Unlike traditional tools, AutoPent leverages **LLM (LLaMA 3.1)** to provide intelligent recommendations, generate remediation steps, and analyze vulnerabilities dynamically.

---

## Key Features

* **Automated Reconnaissance** – Domain, subdomain, and service discovery.
* **Vulnerability Scanning** – Automated scans using Nmap, OpenVAS, and custom scripts.
* **Exploitation Engine** – Metasploit-based automated exploitation with controlled payloads.
* **Privilege Escalation** – Post-exploitation privilege escalation & persistence detection.
* **AI Security Analysis** – LLaMA 3.1 for intelligent vulnerability assessment & mitigation strategies.
* **Automated Reports** – Professional, compliance-ready PDF/HTML reports.
* **Interactive GUI** – PyQt5-based dashboard for intuitive control and monitoring.

---

## The AutoPent Advantage: A New Paradigm in Security

# Key Features of AutoPent

AutoPent is a first-of-its-kind framework that redefines automated offensive security. 

* **First-of-its-Kind Framework:**
    It introduces a new category of security tooling by bridging the gap between static scanning and dynamic, intelligent analysis.

* **True End-to-End Integration:**
    AutoPent is a single, seamless framework that manages the entire offensive security workflow, including:
    * Reconnaissance
    * Multi-layered scanning
    * Automated exploitation
    * Privilege escalation
    * AI-driven reporting

* **AI-Powered Decision Making:**
    It is the first open-source framework to use a Large Language Model (LLaMA 3.1) at its core. This allows it to:
    * **Understand** vulnerabilities in context.
    * Prioritize risks intelligently.
    * Generate actionable remediation strategies.

* **From Data to Intelligence:**
    The AI engine processes raw scan data and correlates findings to transform security "noise" into a clear, prioritized list of exploitable threats.

* **Unified Command Center:**
    It features an intuitive PyQt5 GUI that acts as a single dashboard for managing complex penetration tests, making advanced security accessible without juggling multiple command-line tools.

---

## Tech Stack

* **Languages:** Python 3.11
* **Frameworks:** PyQt5, Flask (for backend APIs)
* **Libraries:**

  * Recon: `scapy`, `sublist3r`, `shodan`
  * Scanning: `nmap`, `openvas_lib`
  * Exploitation: `msfrpc`, `pwntools`
  * AI/ML: `transformers`, `llama-index`, `langchain`
  * Reporting: `reportlab`, `jinja2`, `pdfkit`
* **Databases:** SQLite for session & scan data
* **AI Model:** **LLaMA 3.1** for contextual security insights

---
## AutoPent Project Workflow: A Seven-Step Process

This document outlines the seven key stages of the AutoPent project, from initial reconnaissance to the final user interface. Each step leverages specific tools and methodologies to create a comprehensive, automated offensive security framework.

---

## Step 1: Reconnaissance & Target Discovery

This initial phase involves collecting as much information as possible about the target system to identify potential attack vectors before launching any exploits. The primary goal is to map the attack surface by extracting DNS records, IP addresses, and exposed services.

For this, we will use the following OSINT (Open-Source Intelligence) API keys:

* **Shodan:** Scans the internet for open ports and exposed devices. It is best suited for IoT, open ports, and banner grabbing.
* **BinaryEdge:** Provides IP scanning data and device fingerprinting. It excels at mass scanning, which helps in detecting data vulnerabilities, and is also useful for botnet and malware hunting.
* **Onyphe:** Specializes in threat intelligence and darknet analysis, providing capabilities like dark web tracking.

---

## Step 2: Vulnerability Scanning

This process automates the detection of misconfigurations, outdated software, and exploitable vulnerabilities in web applications, networks, and databases.

* **NIKTO:**
    * **Key Features:** Checks for outdated software versions and security misconfigurations, identifies exposed sensitive files (e.g., admin panels, backup files), and provides fast scanning with minimal false positives.
    * **Purpose:** Helps in the early detection of security loopholes before manual testing.

* **SQLMap:**
    * **Key Features:** Automatic SQL Injection testing, database enumeration, supports multiple database types, and can bypass security measures.
    * **Purpose:** Helps to uncover sensitive data leaks, unauthorized access, and database misconfigurations.

* **Nmap:**
    * **Key Features:** Port scanning, vulnerability detection (via NSE scripts), service fingerprinting, and Firewall/IDS detection.
    * **Purpose:** Crucial for identifying weak services, misconfigurations, and open ports on a network.

---

## Step 3: Exploitation & Attack Automation

This step aims to determine the actual risk posed by identified vulnerabilities by simulating real-world cyberattacks in a controlled manner.

* **Socket:**
    * Python's socket programming allows for creating custom exploits to attack vulnerable systems.
    * Attackers can send malicious payloads to web servers, databases, or SSH services.
    * **Project Feature:** It converts a target URL into its IP address, which is then fed to the Metasploit framework for exploitation attacks. This simplifies the process for the user, who only needs to provide a URL.

* **Metasploit:**
    * One of the most widely used penetration testing frameworks that helps security professionals discover, exploit, and validate vulnerabilities.
    * It automates vulnerability exploitation, payload delivery, and post-exploitation actions.
    * **Integration:** It uses an RPC server to connect to a Python script, which automates the exploitation process and can cycle through multiple payloads.

---

## Step 4: Privilege Escalation

Privilege escalation is the process of gaining higher-level access to a system or network, typically moving from a low-privileged user to an administrator or root user. This is achieved by exploiting security misconfigurations, vulnerabilities, or weak permissions.

* **WinPEAS (Windows Privilege Escalation Awesome Scripts):**
    * Detects weak file permissions, unquoted service paths, and passwords stored in plaintext.
    * Identifies Windows vulnerabilities that allow privilege escalation.
    * Finds misconfigured services, registry settings, and scheduled tasks.

* **LinPEAS (Linux Privilege Escalation Awesome Scripts):**
    * Detects sudo misconfigurations, SUID binaries, and writable files.
    * Finds known kernel exploits that allow for privilege escalation.
    * Identifies hardcoded credentials and environment variables containing sensitive data.

---

## Step 5: Source Code Analysis

This is the process of examining application code to identify security vulnerabilities, logic flaws, and coding errors that could be exploited by attackers.

* **Haiku (Claude 3.5):**
    * An AI-powered static code analysis tool that helps developers identify security vulnerabilities and coding errors.
    * Supports multiple programming languages (e.g., Java, Python, JavaScript).
    * **Claude 3.5 Haiku** is the next-generation model, offering greater speed and improved skill across the board. It provides more efficient source code analysis and gives more detailed insights into found vulnerabilities.
    * **Benefit:** Provides fix recommendations for vulnerabilities and helps automate secure code reviews in DevSecOps pipelines.

---

## Step 7: User Interface and User Experience (UI/UX)

A graphical user interface (GUI) is used to make the framework accessible and easy for users to navigate. It provides a visual representation of the modules running in the backend.

* **Key Features:**
    * **Integrated Security Testing:** A single dashboard to launch and monitor all tests.
    * **Report Generation & Export:** Saves results as PDF or text files, allowing users to easily find and review the reports and see which modules were successful.

* **Flask:**
    * A lightweight web framework used for the backend.
    * **Handles HTTP Requests:** Connects the front-end UI to the backend modules.
    * **Supports API Calls:** Enables the remote execution of penetration testing tasks.
    * **Integrates with Databases & Logging Systems:** Stores pentesting reports, providing access to historical data.

* **PyQt5:**
    * A set of Python bindings for the Qt application framework, used to build the GUI.
    * **Cross-Platform & Feature-Rich:** Build GUI applications for Windows, macOS, and Linux with over 600 built-in widgets.
    * **Event-Driven Programming:** Uses a signals and slots mechanism for seamless event handling.
    * **Drag & Drop UI with Qt Designer:** Allows for visual creation of UIs, which can then be converted into Python code.

---

<img width="1395" height="710" alt="Screenshot 2025-09-14 022436" src="https://github.com/user-attachments/assets/eb80fc1b-6569-43dc-94cb-aa73a46baf90" />

---

## Why AutoPent?

![WhatsApp Image 2025-08-24 at 16 55 46_fc85ad18](https://github.com/user-attachments/assets/98460812-1cb4-45cc-9b6d-778f3cfb55b1)


---

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

*   Python 3.x
*   External tools like `nmap`, `nikto`, and `sqlmap` should be installed and available in your system's PATH.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Abhinavmehra2004/CyberShield-Hakathon-Autopenters-.git
    ```

2.  **Navigate to the source code directory:**
    ```sh
    cd CyberShield-Hakathon-Autopenters-/SourceCode
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```sh
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

---
