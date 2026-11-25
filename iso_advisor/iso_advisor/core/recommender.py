"""موتور پیشنهاد آفلاین: تطبیق کلمات کلیدی + قاعده‌ی حوزه‌ی فعالیت (دوزبانه)."""
import json
import re
from pathlib import Path

from .i18n import t

DATA = Path(__file__).parent.parent / "data"
KB_PATH = DATA / "standards.json"
KB_EN_PATH = DATA / "standards_en.json"


def load_kb(lang: str = "fa"):
    kb = json.loads(KB_PATH.read_text(encoding="utf-8"))
    en = json.loads(KB_EN_PATH.read_text(encoding="utf-8")) if KB_EN_PATH.exists() else {}
    for s in kb:
        extra = en.get(s["id"], {})
        s["keywords"] = list(dict.fromkeys(s["keywords"] + extra.get("keywords", [])))  # فارسی و انگلیسی با هم
        if lang == "en" and extra.get("questions"):
            s["questions"] = extra["questions"]
        s["title"] = s["title_en"] if lang == "en" else s["title_fa"]
    return kb


def normalize(text: str) -> str:
    text = text.lower().replace("ي", "ی").replace("ك", "ک").replace("\u200c", " ")
    return re.sub(r"[^\w\s]", " ", text)


def recommend(description: str, sector: str | None = None, top_n: int = 5, lang: str = "fa"):
    text = normalize(description or "")
    results = []
    for std in load_kb(lang):
        score, reasons = 0, []
        for kw in std["keywords"]:
            if normalize(kw) in text:
                score += 2
                reasons.append(t(lang, "r_kw", kw=kw))
        if sector and sector in std["sectors"]:
            score += 3
            from .i18n import sector_label
            reasons.append(t(lang, "r_sector", s=sector_label(sector, lang)))
        if std.get("universal"):
            score += 1
            reasons.append(t(lang, "r_univ"))
        if score > 0:
            results.append({
                "id": std["id"],
                "title": f'{std["id"]} - {std["title"]}',
                "match_percent": min(100, round(score / 10 * 100)),
                "reasons": reasons,
            })
    results.sort(key=lambda r: r["match_percent"], reverse=True)
    return results[:top_n]
