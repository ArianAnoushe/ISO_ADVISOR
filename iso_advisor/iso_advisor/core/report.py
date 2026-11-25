"""ساخت گزارش HTML و CSV (دوزبانه، با پانویس)."""
import csv
import html
import io
from datetime import datetime

from .i18n import t


def to_html(org: str, result: dict, plan: str, mode: str, lang: str = "fa") -> bytes:
    e = html.escape
    rtl = lang == "fa"
    rows = "".join(f'<tr><td>{e(a["question"])}</td><td>{e(a["answer"])}</td><td>{a["score"]}</td></tr>' for a in result["answers"])
    gaps = "".join(f'<li><b>{e(g["priority"])}</b>: {e(g["question"])}</li>' for g in result["gaps"]) or f'<li>{t(lang, "rep_nogaps")}</li>'
    doc = f"""<!doctype html><html lang="{lang}" dir="{'rtl' if rtl else 'ltr'}"><head><meta charset="utf-8"><title>{t(lang, "rep_title")}</title>
<style>body{{font-family:Tahoma,sans-serif;max-width:900px;margin:30px auto;line-height:1.9}}
table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #bbb;padding:6px}}th{{background:#eee}}
.score{{font-size:2em;color:#6c5ce7}}pre{{white-space:pre-wrap;background:#f7f7f7;padding:10px}}
.foot{{margin-top:40px;text-align:center;color:#777;border-top:1px solid #ddd;padding-top:10px}}</style></head><body>
<h1>{t(lang, "rep_title")}</h1>
<p>{t(lang, "rep_org")}: <b>{e(org or t(lang, "rep_unknown"))}</b> | {t(lang, "rep_std")}: <b>{e(result["title"])}</b> | {t(lang, "rep_date")}: {datetime.now():%Y-%m-%d %H:%M} | {t(lang, "rep_mode")}: {e(mode)}</p>
<p class="score">{result["percent"]}% — {t(lang, "rep_level")}: {e(result["level"])}</p>
<h2>{t(lang, "rep_details")}</h2><table><tr><th>{t(lang, "col_q")}</th><th>{t(lang, "col_a")}</th><th>{t(lang, "col_s")}</th></tr>{rows}</table>
<h2>{t(lang, "rep_gaps")}</h2><ul>{gaps}</ul><h2>{t(lang, "rep_plan")}</h2><pre>{e(plan)}</pre>
<div class="foot">{t(lang, "footer")}</div></body></html>"""
    return doc.encode("utf-8")


def to_csv(result: dict, lang: str = "fa") -> bytes:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow([t(lang, "rep_std"), t(lang, "col_q"), t(lang, "col_a"), t(lang, "col_s")])
    for a in result["answers"]:
        w.writerow([result["title"], a["question"], a["answer"], a["score"]])
    w.writerow([])
    w.writerow([t(lang, "csv_total"), result["percent"], t(lang, "csv_level"), result["level"]])
    w.writerow([t(lang, "footer")])
    return buf.getvalue().encode("utf-8-sig")
