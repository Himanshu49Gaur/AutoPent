from llama_cpp import Llama
import config
import json

def load_model():
    try:
        llm = Llama(
            model_path=config.LLAMA_MODEL_PATH,
            n_ctx=4096,  # or reduce to 2048 for large prompts
            n_threads=4,  # or set to os.cpu_count()
            use_mlock=False,  # better performance on macOS with low RAM
            use_mmap=True,
            n_gpu_layers=0  # <== Force CPU to avoid GPU memory crash
        )
        print("Model loaded successfully!")
        return llm
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

llm = load_model()

def estimate_tokens(text):
    """Estimate the number of tokens in text (approximate: 1 token ~ 4 chars)."""
    return len(text) // 4 + len(text.split())

def trim_text(text, max_tokens=300):
    """Trim text to fit within max_tokens (approximate)."""
    if estimate_tokens(text) <= max_tokens:
        return text
    
    words = text.split()
    trimmed = []
    current_tokens = 0
    
    for word in words:
        word_tokens = estimate_tokens(word)
        if current_tokens + word_tokens > max_tokens:
            break
        trimmed.append(word)
        current_tokens += word_tokens
    
    return ' '.join(trimmed) + " ... [truncated]"

def summarize_vuln_results(vuln_results):
    """Summarize vuln_results to fit within token limits."""
    summary = {}
    
    # Prioritize Vulnerabilities
    if "Vulnerabilities" in vuln_results:
        summary["Vulnerabilities"] = vuln_results["Vulnerabilities"]
    
    # Summarize scan outputs
    for key in ["Nikto", "SQLMap", "Nmap"]:
        if key in vuln_results:
            # Take first 100 chars of scan output
            summary[key] = vuln_results[key][:100] + (" ..." if len(vuln_results[key]) > 100 else "")
    
    return summary

def generate_security_analysis(vuln_results):
    """Uses AI to analyze summarized vulnerability scan results and suggest fixes."""
    if not llm:
        return "Error: LLaMA model could not be loaded."

    # Summarize and trim to fit ~400 tokens (512 - prompt overhead)
    summarized_results = summarize_vuln_results(vuln_results)
    vuln_text = json.dumps(summarized_results, indent=2)
    vuln_trimmed = trim_text(vuln_text, max_tokens=400)

    prompt = f"""
    You are a cybersecurity expert. Analyze the following vulnerability scan results for a web application:

    🛡️ Vulnerability Scan Results:
    {vuln_trimmed}

    Provide a detailed summary of issues found and recommend prioritized security fixes.
    """
    try:
        output = llm(prompt, max_tokens=800, temperature=0.7)
        return output['choices'][0]['text'] if isinstance(output, dict) else str(output)
    except Exception as e:
        return f"Error generating analysis: {e}"

if __name__ == "__main__":
    vuln_results = {
        "Nikto": "Sample Nikto output " * 1000,  # Simulate large output
        "SQLMap": "Sample SQLMap output " * 1000,
        "Nmap": "Sample Nmap output " * 1000,
        "Vulnerabilities": [("SQL Injection", "exploit/unix/webapp/sqlmap_sqli")]
    }
    report = generate_security_analysis(vuln_results)
    print("\n===== AI Security Analysis Report =====\n")
    print(report)
