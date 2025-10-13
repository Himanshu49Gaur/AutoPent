import requests
import config

def scan_source_code(url):
    """
    Scan the source code of the given URL using Haiku API.
    Returns a formatted string with vulnerability summary.
    """
    headers = {"Authorization": f"Bearer {config.HAIKU_API_KEY}"}
    data = {"target": url}

    try:
        response = requests.post(config.HAIKU_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            scan_data = response.json()

            if "vulnerabilities" not in scan_data:
                return "[!] No vulnerabilities field in response."

            vulnerabilities = scan_data.get("vulnerabilities", [])
            if not vulnerabilities:
                return "[+] No vulnerabilities detected by Haiku."

            formatted = "[+] Vulnerabilities Detected by Haiku:\n"
            for idx, vuln in enumerate(vulnerabilities, 1):
                cwe = vuln.get("cwe", "N/A")
                description = vuln.get("description", "No description provided.")
                severity = vuln.get("severity", "Unknown")
                location = vuln.get("location", "Unknown file/line")
                
                formatted += (
                    f"\n[{idx}] CWE: {cwe}\n"
                    f"    Severity: {severity}\n"
                    f"    Location: {location}\n"
                    f"    Description: {description}\n"
                )

            return formatted

        else:
            return f"[!] Failed to scan source code. HTTP Status Code: {response.status_code}\nResponse: {response.text}"

    except requests.RequestException as e:
        return f"[!] Request to Haiku API failed: {str(e)}"

# Example usage for testing
if __name__ == "__main__":
    url = "https://example.com"
    results = scan_source_code(url)
    print(results)
