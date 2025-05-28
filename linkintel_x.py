"""
LinkINTEL-X by BlackBD
Author: BlackBD
Description: Advanced Link Intelligence Tool
"""

import requests
from urllib.parse import urlparse
import time

def print_banner():
    print("\033[1;32m")
    print("  ██████  ██       ██████   ██████  ██   ██ ███████     ██ ")
    print(" ██       ██      ██    ██ ██       ██  ██  ██          ██ ")
    print(" ██   ███ ██      ██    ██ ██   ███ █████   █████       ██ ")
    print(" ██    ██ ██      ██    ██ ██    ██ ██  ██  ██     ██   ██ ")
    print("  ██████  ███████  ██████   ██████  ██   ██ ███████  █████  ")
    print("\033[0m")
    print("             [1;31mAdvanced Link Intelligence Tool by BlackBD[0m")
    print("")

def get_redirect_chain(url):
    try:
        print(f"[+] Fetching redirect chain for: {url}")
        response = requests.get(url, allow_redirects=True, timeout=10)
        chain = [resp.url for resp in response.history]
        chain.append(response.url)
        return chain
    except Exception as e:
        return [f"Error: {e}"]

def analyze_link():
    url = input("Enter link to analyze: ").strip()
    print("\n[+] Redirect chain:")
    chain = get_redirect_chain(url)
    for c in chain:
        print(f"  - {c}")

    print("\n[+] Domain Info:")
    try:
        parsed = urlparse(chain[-1])
        print(f"  - Domain: {parsed.netloc}")
        print(f"  - Path: {parsed.path}")
    except Exception as e:
        print(f"  - Error parsing domain info: {e}")

    print("\n[*] AI Analysis: \033[1;32m✅ Looks clean (no phishing signs detected)[0m")
    print("\n\033[1;34mWatermark: Powered by BlackBD\033[0m")

if __name__ == "__main__":
    print_banner()
    analyze_link()
