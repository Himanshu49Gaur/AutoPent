import subprocess
import re

def run_command(command, timeout=300):
    """Runs a shell command with a timeout and returns the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "⚠️ Command timed out after {} seconds.".format(timeout)
    except subprocess.SubprocessError as e:
        return f"⚠️ Command failed: {e}"

def run_nikto_scan(target):
    """Runs Nikto web server vulnerability scan."""
    return run_command(f"nikto -h {target}")

def run_sqlmap_scan(target):
    """Runs SQLMap to test for SQL Injection vulnerabilities."""
    return run_command(f"sqlmap -u {target} --batch --risk=3 --level=5")

def run_nmap_nse(target):
    """Runs Nmap NSE scripts to identify known vulnerabilities."""
    return run_command(f"nmap --script vuln {target}")

# Mapping known vulnerabilities to Metasploit exploits
VULN_TO_EXPLOIT = {
    "vsftpd 2.3.4": "exploit/unix/ftp/vsftpd_234_backdoor",
    "Apache Struts": "exploit/multi/http/struts2_exec",
    "SMBv1": "exploit/windows/smb/ms17_010_eternalblue",
    "SQL Injection": "exploit/unix/webapp/sqlmap_sqli",
}

def extract_vulnerabilities(scan_results):
    """Extracts potential vulnerabilities from scan outputs."""
    found_vulnerabilities = []

    # Check for known vulnerable software versions
    for vuln, exploit in VULN_TO_EXPLOIT.items():
        if vuln.lower() in scan_results.lower():
            found_vulnerabilities.append((vuln, exploit))
    
    return found_vulnerabilities

def run_vulnerability_scan(target):
    """Runs all vulnerability scanning tools and stores results in vuln_results."""
    vuln_results = {}

    print("[+] Running Nikto scan...")
    nikto_result = run_nikto_scan(target)
    vuln_results["Nikto"] = nikto_result

    print("[+] Running SQLMap scan...")
    sqlmap_result = run_sqlmap_scan(target)
    vuln_results["SQLMap"] = sqlmap_result

    print("[+] Running Nmap NSE scan...")
    nmap_result = run_nmap_nse(target)
    vuln_results["Nmap"] = nmap_result

    # Combine all results for vulnerability extraction
    all_results = nikto_result + "\n" + sqlmap_result + "\n" + nmap_result
    vulnerabilities = extract_vulnerabilities(all_results)
    vuln_results["Vulnerabilities"] = vulnerabilities

    if vulnerabilities:
        print("[+] Vulnerabilities found!")
        for vuln, exploit in vulnerabilities:
            print(f"  - {vuln} -> Suggested Exploit: {exploit}")
    else:
        print("[-] No known vulnerabilities detected.")

    return vuln_results

if __name__ == "__main__":
    target = "https://demo.testfire.net/login.jsp"
    vuln_results = run_vulnerability_scan(target)
    if vuln_results["Vulnerabilities"]:
        suggested_exploit = vuln_results["Vulnerabilities"][0][1]
        print(f"[+] Running exploitation module: {suggested_exploit}")
