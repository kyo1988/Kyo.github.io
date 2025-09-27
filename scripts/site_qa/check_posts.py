import sys, argparse, re, os, json
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

REQ = ["gate-badge","method-box","mvr","decision-bridge","jsonld-article","og:title","twitter:card","reproline"]
UTM_RE = re.compile(r"utm_source=blog")
INTERNAL_RE = re.compile(r"^/|^https://kyo1988.github.io")

def fetch(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.text

def check_post(html, url):
    soup = BeautifulSoup(html, "lxml")
    res = {"url": url}
    # Gate
    res["gate"] = bool(soup.select_one(".gate-badge"))
    # Method/MVR/Decision
    res["method"] = bool(soup.select_one(".method-box"))
    res["mvr"] = bool(soup.select_one(".mvr"))
    res["decision"] = bool(soup.select_one(".decision-bridge"))
    # JSON-LD
    res["jsonld"] = bool(soup.select_one("#jsonld-article"))
    # OG/Twitter
    res["og"] = bool(soup.find("meta", {"property":"og:title"}))
    res["tw"] = bool(soup.find("meta", {"name":"twitter:card"}))
    # img alt
    imgs = soup.find_all("img")
    res["img_alt"] = all((img.get("alt") or "").strip() for img in imgs) if imgs else True
    # reproduction line
    res["repro"] = bool(soup.select_one(".reproline"))
    # internal links ≥2
    links = [a.get("href","") for a in soup.find_all("a")]
    res["internal_links_ge2"] = sum(1 for h in links if INTERNAL_RE.search(h)) >= 2
    # external CTA UTM
    external = [h for h in links if h.startswith("http") and not h.startswith("https://kyo1988.github.io")]
    res["external_utm"] = all(UTM_RE.search(h) for h in external) if external else True
    return res

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="https://kyo1988.github.io")
    ap.add_argument("--paths", nargs="*", default=[
        "/marketing/2025/09/27/marketing-science-analysis-status.html",
        "/marketing/2025/09/27/moderation-dirichlet-analysis.html",
        "/marketing/2025/09/27/category-entry-points-analysis.html",
        "/marketing/2025/09/27/duplication-of-purchase-near-miss.html",
        "/marketing/2025/09/27/double-jeopardy-analysis-fail.html",
    ])
    args = ap.parse_args()
    rows = []
    for p in args.paths:
        url = urljoin(args.base, p)
        try:
            html = fetch(url)
            rows.append(check_post(html, url))
        except Exception as e:
            rows.append({"url": url, "error": str(e)})

    os.makedirs("results", exist_ok=True)
    path = "results/site_qa_report.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Site QA Report\n\n")
        for r in rows:
            f.write(f"## {r['url']}\n\n")
            if "error" in r:
                f.write(f"- ❌ fetch error: {r['error']}\n\n")
                continue
            f.write(
                "- Gate badge: " + ("✅" if r["gate"] else "❌") + "\n" +
                "- Method box: " + ("✅" if r["method"] else "❌") + "\n" +
                "- Myth vs Reality: " + ("✅" if r["mvr"] else "❌") + "\n" +
                "- Decision Bridge: " + ("✅" if r["decision"] else "❌") + "\n" +
                "- JSON-LD: " + ("✅" if r["jsonld"] else "❌") + "\n" +
                "- OG/Twitter meta: " + ("✅" if (r["og"] and r["tw"]) else "❌") + "\n" +
                "- Image alt texts: " + ("✅" if r["img_alt"] else "❌") + "\n" +
                "- Reproduction line: " + ("✅" if r["repro"] else "❌") + "\n" +
                "- Internal links ≥2: " + ("✅" if r["internal_links_ge2"] else "❌") + "\n" +
                "- External CTAs have UTM: " + ("✅" if r["external_utm"] else "❌") + "\n\n"
            )
    print(path)

if __name__ == "__main__":
    main()
