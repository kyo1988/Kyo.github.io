import requests, os
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
    s = BeautifulSoup(html, "lxml")
    return [l.get("href") for l in s.find_all("link", rel="stylesheet") if l.get("href")]

def abs_url(href):
    if href.startswith("//"):
        return "https:" + href
    if href.startswith("http://") or href.startswith("https://"):
        return href
    if href.startswith("/"):
        return BASE + href
    # relative to page: treat as root-relative for GH Pages safety
    return BASE + "/" + href.lstrip("./")

def main():
    os.makedirs("results", exist_ok=True)
    out_lines = []
    for p in PATHS:
        url = BASE + p
        try:
            r = requests.get(url, timeout=15)
            r.raise_for_status()
        except Exception as e:
            out_lines.append(f"# {url}\nERROR fetch page: {e}\n")
            continue
        hrefs = css_links(r.text)
        if not hrefs:
            out_lines.append(f"# {url}\n(no <link rel=\"stylesheet\"> found)\n")
            continue
        out_lines.append(f"# {url}")
        for href in hrefs:
            u = abs_url(href)
            try:
                rr = requests.get(u, timeout=15)
                code = rr.status_code
                ctype = rr.headers.get("content-type","")
                out_lines.append(f"{href}  ->  {u}  ::  {code}  {ctype}")
            except Exception as e:
                out_lines.append(f"{href}  ->  {u}  ::  ERROR {e}")
        out_lines.append("")
    txt = "\n".join(out_lines)
    print(txt)
    with open("results/css_live_check.txt","w",encoding="utf-8") as f:
        f.write(txt)

if __name__ == "__main__":
    main()
