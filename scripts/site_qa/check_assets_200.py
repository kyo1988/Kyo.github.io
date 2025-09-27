#!/usr/bin/env python3
"""
Site Assets QA - Check CSS 200 status
Verifies that all CSS files load with 200 status and text/css content-type
"""

import requests
import sys
from bs4 import BeautifulSoup

BASE = "https://kyo1988.github.io"
PATHS = [
    "/",  # index
    "/marketing/2025/09/27/marketing-science-analysis-status.html",
    "/marketing/2025/09/27/moderation-dirichlet-analysis.html",
    "/marketing/2025/09/27/category-entry-points-analysis.html",
    "/marketing/2025/09/27/duplication-of-purchase-near-miss.html",
    "/marketing/2025/09/27/double-jeopardy-analysis-fail.html",
]

def css_links(html):
    """Extract CSS links from HTML"""
    soup = BeautifulSoup(html, "lxml")
    return [link.get("href") for link in soup.find_all("link", rel="stylesheet") if link.get("href")]

def check_page(url):
    """Check CSS assets for a single page"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        links = css_links(response.text)
        results = []
        
        for href in links:
            # Normalize URL
            if href.startswith("//"):
                href = "https:" + href
            elif href.startswith("/"):
                href = BASE + href
            
            try:
                css_response = requests.get(href, timeout=10)
                content_type = css_response.headers.get("content-type", "")
                results.append((href, css_response.status_code, content_type))
            except Exception as e:
                results.append((href, "ERROR", str(e)))
        
        return results
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return []

def main():
    """Main function"""
    all_ok = True
    
    for path in PATHS:
        url = BASE + path
        print(f"\n=== Checking {url} ===")
        
        results = check_page(url)
        if not results:
            all_ok = False
            continue
        
        for href, status, content_type in results:
            is_ok = (status == 200 and "text/css" in content_type)
            status_text = "OK" if is_ok else "NG"
            print(f"  {href} : {status} {content_type} [{status_text}]")
            all_ok &= is_ok
    
    print(f"\n=== Overall Result: {'PASS' if all_ok else 'FAIL'} ===")
    sys.exit(0 if all_ok else 2)

if __name__ == "__main__":
    main()