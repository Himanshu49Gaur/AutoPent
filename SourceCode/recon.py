import requests
import socket
import whois
import dns.resolver
import shodan
import config
import re

def is_ip_address(domain):
    """Check if the input is an IP address."""
    ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(ip_pattern, domain))

def clean_domain(domain):
    """Remove port, path, or scheme from domain."""
    # Remove scheme (http://, https://)
    domain = re.sub(r'^https?://', '', domain)
    # Remove path and query
    domain = domain.split('/')[0]
    # Remove port
    domain = domain.split(':')[0]
    return domain.strip().lower()

def get_ip_address(domain):
    """Resolve domain to IP address, handling IP inputs and localhost directly."""
    domain = clean_domain(domain)
    
    # Handle localhost explicitly
    if domain in ['localhost', '127.0.0.1']:
        return '127.0.0.1', '🌐 IP Address: 127.0.0.1'
    
    # If the input is already an IP address, return it
    if is_ip_address(domain):
        return domain, f'🌐 IP Address: {domain}'
    
    # For hostnames, attempt DNS resolution
    try:
        ip = socket.gethostbyname(domain)
        return ip, f'🌐 IP Address: {ip}'
    except Exception as e:
        return None, f'⚠️ Could not resolve domain to IP: {e}'

def get_whois_info(domain):
    """Perform WHOIS lookup, skipping for IP addresses."""
    domain = clean_domain(domain)
    
    # Skip WHOIS for IP addresses or localhost
    if is_ip_address(domain) or domain in ['127.0.0.1', 'localhost']:
        return '⚠️ WHOIS lookup skipped for IP address or localhost.'
    
    # Validate domain format (basic check for TLD)
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
        return '⚠️ WHOIS lookup skipped: Invalid domain format.'
    
    try:
        info = whois.query(domain)
        if info:
            return f'🔍 WHOIS Info:\n{info.__dict__}'
        else:
            return '⚠️ WHOIS lookup returned no data.'
    except Exception as e:
        return f'⚠️ WHOIS lookup failed: {e}'

def get_dns_records(domain):
    """Retrieve DNS records for the domain."""
    domain = clean_domain(domain)
    
    if is_ip_address(domain) or domain in ['127.0.0.1', 'localhost']:
        return '⚠️ DNS lookup skipped for IP address or localhost.'
    
    records = {}
    try:
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                records[record_type] = [r.to_text() for r in answers]
            except Exception:
                records[record_type] = []
        return f'📡 DNS Records:\n{records}'
    except Exception as e:
        return f'⚠️ DNS resolution failed: {e}'

def get_headers(url):
    """Fetch HTTP headers from the URL."""
    try:
        response = requests.get(url, timeout=5)
        return f'📁 Response Headers:\n{response.headers}'
    except Exception as e:
        return f'⚠️ Error retrieving headers: {e}'

def shodan_lookup(ip):
    """Perform Shodan lookup for the IP."""
    if not ip or ip in ['127.0.0.1']:
        return '⚠️ Shodan lookup skipped for invalid or localhost IP.'
    
    try:
        api = shodan.Shodan(config.SHODAN_API_KEY)
        result = api.host(ip)
        return f'🔎 Shodan Results:\nOpen Ports: {result.get("ports", [])}\nVulnerabilities: {result.get("vulns", [])}'
    except Exception as e:
        return f'⚠️ Shodan lookup failed: {e}'

def binaryedge_lookup(ip):
    """Perform BinaryEdge lookup for the IP."""
    if not ip or ip in ['127.0.0.1']:
        return '⚠️ BinaryEdge lookup skipped for invalid or localhost IP.'
    
    url = f'https://api.binaryedge.io/v2/query/ip/{ip}'
    headers = {'X-Key': config.BINARYEDGE_API_KEY}
    try:
        response = requests.get(url, headers=headers)
        return f'🚀 BinaryEdge Results:\n{response.json()}'
    except Exception as e:
        return f'⚠️ BinaryEdge lookup failed: {e}'

def onyphe_lookup(ip):
    """Perform ONYPHE lookup for the IP."""
    if not ip or ip in ['127.0.0.1']:
        return '⚠️ ONYPHE lookup skipped for invalid or localhost IP.'
    
    url = f'https://www.onyphe.io/api/v2/simple/geoloc/{ip}'
    headers = {'Authorization': f'apikey {config.ONYPHE_API_KEY}'}
    try:
        response = requests.get(url, headers=headers)
        return f'📍 ONYPHE Results:\n{response.json()}'
    except Exception as e:
        return f'⚠️ ONYPHE lookup failed: {e}'

def run_recon(domain, url):
    """Run reconnaissance tasks."""
    ip, ip_result = get_ip_address(domain)
    results = {
        "IP Address": ip_result,
        "WHOIS": get_whois_info(domain),
        "DNS Records": get_dns_records(domain),
        "Response Headers": get_headers(url),
    }

    if ip and ip != '127.0.0.1':
        results.update({
            "Shodan": shodan_lookup(ip),
            "BinaryEdge": binaryedge_lookup(ip),
            "ONYPHE": onyphe_lookup(ip),
        })

    return results

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    url = "https://example.com"
    recon = run_recon(domain, url)
    for k, v in recon.items():
        print(f"\n[{k}]\n{v}")
