import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog
from recon import run_recon
from scanning import run_vulnerability_scan
from exploitation import run_exploit
from ai_analysis import generate_security_analysis
from reporting import generate_security_report
from urllib.parse import urlparse

class AutoPentGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.title_label = QLabel("AutoPent: Automated Penetration Testing Framework", self)
        layout.addWidget(self.title_label)
        
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter Target URL: https://example.com")
        layout.addWidget(self.url_input) 
        
        self.start_button = QPushButton("Start Security Test", self)
        self.start_button.clicked.connect(self.run_tests)
        layout.addWidget(self.start_button)
        
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)
        
        self.download_button = QPushButton("Download Report", self)
        self.download_button.setEnabled(False)
        self.download_button.clicked.connect(self.download_report)
        layout.addWidget(self.download_button)
        
        self.setLayout(layout)
        self.setWindowTitle("AutoPent GUI")
        self.setGeometry(300, 200, 600, 400)
        
    def run_tests(self):
        target_url = self.url_input.text()

        if not target_url:
            self.output_text.append("Please enter a target URL.")
            return

        parsed_url = urlparse(target_url)
        domain = parsed_url.hostname
        if not domain:
            self.output_text.append("Invalid URL: No hostname found.")
            return

        self.output_text.append("Running Reconnaissance...")
        recon_results = run_recon(domain, target_url)
        if not recon_results.get('IP Address', '').startswith('🌐'):
            self.output_text.append(f"Reconnaissance failed: {recon_results['IP Address']}")
        else:
            self.output_text.append("Reconnaissance Completed!\n")
        
        self.output_text.append("Running Vulnerability Scan...")
        vuln_results = run_vulnerability_scan(target_url)
        self.output_text.append("Vulnerability Scan Completed!\n")
        
        self.output_text.append("Attempting Exploitation...")
        exploit_results = run_exploit(target_url, recon_results, vuln_results)
        if not exploit_results.get('success', False) and 'Could not resolve' in exploit_results.get('message', ''):
            self.output_text.append(f"Exploitation failed: {exploit_results['message']}")
            return
        self.output_text.append("Exploitation Completed!\n")
        
        self.output_text.append("Generating AI Security Analysis...")
        ai_report = generate_security_analysis(vuln_results)
        self.output_text.append("AI Analysis Completed!\n")
        
        self.output_text.append("Generating Final Report...")
        self.report_path = generate_security_report(
            target_url, recon_results, vuln_results, exploit_results, ai_report
        )
        if not self.report_path:
            self.output_text.append("Failed to generate report.")
            return
        self.output_text.append("Report Generated Successfully!\n")

        self.download_button.setEnabled(True)

    def download_report(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Report", "security_report.pdf", "PDF Files (*.pdf)")
        if save_path:
            with open(self.report_path, 'rb') as report_file:
                with open(save_path, 'wb') as save_file:
                    save_file.write(report_file.read())
            self.output_text.append(f"Report saved to: {save_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = AutoPentGUI()
    gui.show()
    sys.exit(app.exec_())
