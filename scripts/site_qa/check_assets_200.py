import requests, sys
from bs4 import BeautifulSoup

BASE = "https://kyo1988.github.io"
PATHS = [
  "/marketing/2025/09/27/marketing-science-analysis-status.html",
  "/marketing/2025/09/27/moderation-dirichlet-analysis.html",
  "/marketing/2025/09/27/category-entry-points-analysis.html",
  "/marketing/2025/09/27/duplication-of-purchase-near-miss.html",
  "/marketing/2025/09/27/double-jeopardy-analysis-fail.html",
]

def css_links(html):
    s = BeautifulSoup(html, "lxml")
    return [l.get("href") for l in s.find_all("link", rel="stylesheet") if l.get("href")]

def check(u):
    r = requests.get(u, timeout=10); r.raise_for_status()
    links = css_links(r.text)
    results = []
    for href in links:
        if href.startswith("//"): href = "https:" + href
        if href.startswith("/"):  href = BASE + href
        rr = requests.get(href, timeout=10)
        results.append((href, rr.status_code, rr.headers.get("content-type","")))
    return results

def main():
    ok = True
    for p in PATHS:
        u = BASE + p
        try:
            rows = check(u)
        except Exception as e:
            print(f"[ERROR] fetch {u}: {e}")
            ok = False
            continue
        for href, code, ct in rows:
            good = (code == 200 and "text/css" in ct)
            print(f"{u} -> {href} : {code} {ct} {'OK' if good else 'NG'}")
            ok &= good
    sys.exit(0 if ok else 2)

if __name__ == "__main__":
    main()
