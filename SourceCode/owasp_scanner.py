import requests
from haiku import scan_source_code


def check_sql_injection(url):
    payload = "' OR '1'='1"
    try:
        response = requests.post(url + "/login", data={"username": payload, "password": payload})
        if "Login Successful" in response.text:
            return "❌ SQL Injection Detected!"
    except Exception as e:
        return f"⚠️ Error testing SQL Injection: {e}"
    return "✅ Secure against SQL Injection."


def check_ssrf(url):
    internal_url = "http://127.0.0.1:22"
    try:
        response = requests.get(url + "/fetch", params={"url": internal_url}, timeout=5)
        if "OpenSSH" in response.text:
            return "❌ SSRF Detected! Can access internal services."
    except Exception as e:
        return f"⚠️ Error testing SSRF: {e}"
    return "✅ Secure against SSRF."


def check_debug_mode(url):
    try:
        response = requests.get(url + "/debug")
        if "insecure_secret_key" in response.text or "Traceback" in response.text:
            return "❌ Debug Mode Detected! Sensitive info exposed."
    except Exception as e:
        return f"⚠️ Error checking debug mode: {e}"
    return "✅ Secure: Debug mode disabled."


def check_weak_auth(url):
    try:
        response = requests.get(url + "/admin", params={"token": "12345"})
        if "Welcome" in response.text:
            return "❌ Weak Authentication Detected! Hardcoded token in use."
    except Exception as e:
        return f"⚠️ Error checking weak auth: {e}"
    return "✅ Secure authentication."


def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url + "/search", params={"q": payload})
        if payload in response.text:
            return "❌ XSS Detected! Payload reflected in response."
    except Exception as e:
        return f"⚠️ Error checking XSS: {e}"
    return "✅ Secure against XSS."


def check_open_redirect(url):
    try:
        response = requests.get(url + "/redirect", params={"url": "http://evil.com"}, allow_redirects=False)
        if response.status_code in [301, 302] and "evil.com" in response.headers.get("Location", ""):
            return "❌ Open Redirect Detected!"
    except Exception as e:
        return f"⚠️ Error checking open redirect: {e}"
    return "✅ Secure against Open Redirect."


def run_owasp_tests(target_url):
    return {
        "SQL Injection": check_sql_injection(target_url),
        "SSRF": check_ssrf(target_url),
        "Debug Mode": check_debug_mode(target_url),
        "Weak Authentication": check_weak_auth(target_url),
        "XSS (Cross-Site Scripting)": check_xss(target_url),
        "Open Redirect": check_open_redirect(target_url),
        "Source Code Analysis": scan_source_code(target_url)
    }
