# AutoPent – Source Code

AutoPent is an AI-powered penetration testing framework that automates reconnaissance, vulnerability scanning, exploitation, reporting, and AI-driven analysis.

---

## Project Structure

| File/Module            | Purpose                                                         |
|------------------------|-----------------------------------------------------------------|
| `ai_analysis.py`       | Integrates LLaMA 3.1 for AI-based vulnerability assessment.     |
| `app.py`               | Main application entry point and API server setup.              |
| `autopent.py`          | Orchestrates end-to-end penetration testing workflow.           |
| `config.py`            | Configuration settings and environment management.              |
| `exploitation.py`      | Handles exploitation phase and payload management.              |
| `haiku.py`             | Utility/helper functions for the framework.                     |
| `owasp_scanner.py`     | OWASP vulnerability scanning module.                            |
| `recon.py`             | Reconnaissance and information gathering.                       |
| `reporting.py`         | Report generation and results formatting.                       |
| `requirements.txt`     | Python dependencies and package requirements.                   |
| `scanning.py`          | Generic vulnerability scanning logic.                           |

---

## Features

- Automated reconnaissance, scanning, exploitation, reporting, and AI analysis.
- Modular design for extendability and custom workflows.
- GPU-accelerated AI analysis (optimized for RTX 3050 and above).
- Human-readable, actionable security reports.

---

## Getting Started

1. **Install dependencies**

2. **Configure environment**
- Edit `config.py` for settings such as API keys, GPU settings, and scan parameters.

3. **Run the framework**

