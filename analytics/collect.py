#!/usr/bin/env python3
"""Collect GitHub's rolling 14-day traffic and build a public Markdown dashboard."""
import datetime as dt
import json
import os
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
DATA = ROOT / "traffic.json"
TOKEN = os.environ["GH_TOKEN"]
REPO = os.environ.get("GITHUB_REPOSITORY", "danilovida/SOC-CORE")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
           "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "soc-core-traffic-dashboard"}

def get(endpoint):
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/traffic/{endpoint}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def main():
    old = json.loads(DATA.read_text()) if DATA.exists() else {"daily": {}, "snapshots": []}
    views, clones, referrers, paths = (get(x) for x in ("views", "clones", "popular/referrers", "popular/paths"))
    days = old.setdefault("daily", {})
    for name, payload in (("views", views), ("clones", clones)):
        for item in payload.get(name, []):
            date = item["timestamp"][:10]
            days.setdefault(date, {})[name] = item["count"]
            days[date][f"unique_{name}"] = item["uniques"]
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    snapshots = old.setdefault("snapshots", [])
    snapshots[:] = [x for x in snapshots if x["date"] != today]
    snapshots.append({"date": today, "views_14d": views["count"], "unique_visitors_14d": views["uniques"],
                      "clones_14d": clones["count"], "unique_cloners_14d": clones["uniques"],
                      "referrers": referrers, "popular_paths": paths})
    snapshots.sort(key=lambda x: x["date"])
    DATA.write_text(json.dumps(old, indent=2, ensure_ascii=False) + "\n")
    latest = snapshots[-1]
    lines = ["# SOC CORE — GitHub Traffic Dashboard", "",
             f"**Last collection (UTC):** {today} · [Repository](https://github.com/{REPO})", "",
             "## Last 14 days (GitHub rolling totals)", "",
             "| Views | Unique visitors | Clones | Unique cloners |",
             "|---:|---:|---:|---:|",
             f"| {latest['views_14d']} | {latest['unique_visitors_14d']} | {latest['clones_14d']} | {latest['unique_cloners_14d']} |",
             "", "## Daily traffic", "",
             "| Date (UTC) | Views | Unique visitors | Clones | Unique cloners |",
             "|---|---:|---:|---:|---:|"]
    for date, v in sorted(days.items(), reverse=True):
        lines.append(f"| {date} | {v.get('views', '—')} | {v.get('unique_views', '—')} | {v.get('clones', '—')} | {v.get('unique_clones', '—')} |")
    lines += ["", "## Top referring sites (latest snapshot)", "",
              "| Site | Views | Unique visitors |", "|---|---:|---:|"]
    for x in latest["referrers"]:
        lines.append(f"| {x['referrer']} | {x['count']} | {x['uniques']} |")
    lines += ["", "## Popular paths (latest snapshot)", "",
              "| Path | Views | Unique visitors |", "|---|---:|---:|"]
    for x in latest["popular_paths"]:
        lines.append(f"| `{x['path']}` | {x['count']} | {x['uniques']} |")
    lines += ["", "## Notes", "",
              "- GitHub only exposes a rolling ~14-day traffic window; older visits cannot be recovered.",
              "- The first collection imports all daily data currently available from GitHub.",
              "- Unique visitors are deduplicated only within the period reported by GitHub; do not sum daily uniques.",
              "- This dashboard does not identify individual visitors, IP addresses, or private user data.",
              "- Historical daily counts are retained from successive collections. Missing days mean no captured data, not necessarily zero visits.",
              "", "[Raw traffic history](traffic.json)"]
    (ROOT / "README.md").write_text("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
