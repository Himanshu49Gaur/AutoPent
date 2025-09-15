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
