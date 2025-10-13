from llama_cpp import Llama
import config
import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import os
from datetime import datetime

# Load LLaMA using llama_cpp
def load_model():
    try:
        llm = Llama(
            model_path=config.LLAMA_MODEL_PATH,
            n_gpu_layers=50,
            use_mlock=True,
            use_mmap=True
        )
        print("Model loaded successfully!")
        return llm
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

llm = load_model()

def truncate_vuln_info(vuln_info, max_length=1000):
    """Truncate vulnerability info to avoid token limit issues."""
    if len(vuln_info) > max_length:
        return vuln_info[:max_length] + "\n... (truncated for analysis)"
    return vuln_info

def generate_security_analysis(vuln_info):
    """Uses AI to analyze vulnerabilities and suggest fixes."""
    if not llm:
        return "Error: LLaMA model could not be loaded."

    # Truncate vuln_info to avoid token limit
    vuln_info = truncate_vuln_info(vuln_info)

    prompt = f"""
    You are a cybersecurity expert. Analyze the following vulnerability information for a website. 
    Identify all issues and suggest detailed fixes for each:

    {vuln_info}
    """
    try:
        output = llm(prompt, max_tokens=800, temperature=0.7)
        return output['choices'][0]['text']
    except Exception as e:
        return f"Error generating analysis: {e}"

def generate_security_report(url, recon_data, vuln_data, exploit_data, ai_text):
    """Generate a security report with the provided data."""
    # Extract domain from URL for filename
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    
    # Generate unique report filename based on timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"security_report_{domain}_{timestamp}.pdf"

    try:
        # Set up ReportLab document
        doc = SimpleDocTemplate(
            report_filename,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )
        styles = getSampleStyleSheet()
        
        # Define custom styles
        title_style = ParagraphStyle(
            name='Title',
            parent=styles['Title'],
            fontSize=18,
            spaceAfter=12,
            textColor=colors.HexColor("#2c3e50")
        )
        heading_style = ParagraphStyle(
            name='Heading2',
            parent=styles['Heading2'],
            fontSize=14,
            spaceBefore=12,
            spaceAfter=6,
            textColor=colors.HexColor("#34495e")
        )
        body_style = ParagraphStyle(
            name='Body',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            leading=12,
            backColor=colors.HexColor("#f8f9fa"),
            borderPadding=5,
            borderWidth=0.5,
            borderColor=colors.grey
        )

        # Build content
        content = []

        # Title
        content.append(Paragraph("AutoPent Security Report", title_style))
        content.append(Spacer(1, 0.2*inch))

        # Target Section
        content.append(Paragraph("Target", heading_style))
        content.append(Paragraph(url, body_style))
        content.append(Spacer(1, 0.1*inch))

        # Reconnaissance Results
        content.append(Paragraph("Reconnaissance Results", heading_style))
        recon_text = json.dumps(recon_data, indent=2).replace('\n', '<br/>')
        content.append(Paragraph(recon_text, body_style))
        content.append(Spacer(1, 0.1*inch))

        # Vulnerability Scan Results
        content.append(Paragraph("Vulnerability Scan Results", heading_style))
        vuln_text = json.dumps(vuln_data, indent=2).replace('\n', '<br/>')
        content.append(Paragraph(vuln_text, body_style))
        content.append(Spacer(1, 0.1*inch))

        # Exploitation Results
        content.append(Paragraph("Exploitation Results", heading_style))
        exploit_text = json.dumps(exploit_data, indent=2).replace('\n', '<br/>')
        content.append(Paragraph(exploit_text, body_style))
        content.append(Spacer(1, 0.1*inch))

        # AI-Powered Recommendations
        content.append(Paragraph("AI-Powered Recommendations", heading_style))
        ai_text = ai_text.replace('\n', '<br/>')
        content.append(Paragraph(ai_text, body_style))
        content.append(Spacer(1, 0.1*inch))

        # Build PDF
        doc.build(content)
        print(f"Security report generated at {report_filename}")
        return report_filename

    except Exception as e:
        print(f"Error generating report: {e}")
        return None

# Example usage
if __name__ == "__main__":
    from recon import run_recon
    from scanning import run_vulnerability_scan
    from exploitation import run_exploit
    domain = "example.com"
    url = "https://example.com"
    recon_data = run_recon(domain, url)
    vuln_data = run_vulnerability_scan(url)
    exploit_data = run_exploit(url)
    ai_text = generate_security_analysis(json.dumps(vuln_data, indent=2))
    generate_security_report(url, recon_data, vuln_data, exploit_data, ai_text)
