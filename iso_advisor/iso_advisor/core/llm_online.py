"""حالت آنلاین: هر API سازگار با فرمت OpenAI (پیش‌فرض: Grok از xAI؛ برای Groq مدل خودکار انتخاب می‌شود)."""
import json
import os
import re

import requests

DEFAULT_BASE_URL = "https://api.x.ai/v1"
DEFAULT_MODEL = "grok-3-mini"
GROQ_DEFAULT_MODEL = "openai/gpt-oss-20b"


def _build_config(api_key, base_url, model) -> dict:
    return {
        "api_key": (api_key or os.getenv("XAI_API_KEY") or os.getenv("LLM_API_KEY") or "").strip(),
        "base_url": (base_url or os.getenv("LLM_BASE_URL") or DEFAULT_BASE_URL).strip().rstrip("/"),
        "model": (model or os.getenv("LLM_MODEL") or DEFAULT_MODEL).strip(),
    }


def get_config(api_key=None, base_url=None, model=None) -> dict:
    cfg = _build_config(api_key, base_url, model)
    if "groq.com" in cfg["base_url"] and cfg["model"] == DEFAULT_MODEL:
        cfg["model"] = GROQ_DEFAULT_MODEL
    return cfg


def _chat(messages, cfg, timeout=40) -> str:
    r = requests.post(
        f'{cfg["base_url"]}/chat/completions',
        headers={"Authorization": f'Bearer {cfg["api_key"]}', "Content-Type": "application/json"},
        json={"model": cfg["model"], "messages": messages, "temperature": 0.2},
        timeout=timeout,
    )
    if r.status_code >= 400:
        try:
            detail = r.json()["error"]["message"]
        except Exception:
            detail = r.text[:200]
        raise RuntimeError(f"HTTP {r.status_code}: {detail}")
    return r.json()["choices"][0]["message"]["content"]


def parse_json_array(text: str):
    m = re.search(r"\[.*\]", text, re.DOTALL)
    if not m:
        raise ValueError("invalid JSON from model")
    return json.loads(m.group(0))


def _lang_name(lang):
    return "English" if lang == "en" else "فارسی"


def recommend_online(description, sector, kb, cfg, top_n=5, lang="fa"):
    catalog = "\n".join(f'{s["id"]}: {s["title_fa"]} ({s["title_en"]})' for s in kb)
    prompt = (
        "You are an ISO standards consultant. Based on the organization description, pick the most suitable standards from the list.\n"
        f"List:\n{catalog}\n\nSector: {sector or 'unknown'}\nDescription: {description}\n\n"
        f'Return ONLY a JSON array (no other text) with at most {top_n} items like: '
        f'[{{"id":"ISO9001","match_percent":85,"reason":"short reason in {_lang_name(lang)}"}}]'
    )
    items = parse_json_array(_chat([{"role": "user", "content": prompt}], cfg))
    kb_by_id = {s["id"]: s for s in kb}
    out = []
    for it in items:
        sid = str(it.get("id", "")).strip()
        if sid in kb_by_id:
            out.append({
                "id": sid,
                "title": f'{sid} - {kb_by_id[sid]["title"]}',
                "match_percent": max(0, min(100, int(it.get("match_percent", 50)))),
                "reasons": [str(it.get("reason", "AI"))],
            })
    if not out:
        raise ValueError("model returned no valid standard")
    out.sort(key=lambda r: r["match_percent"], reverse=True)
    return out[:top_n]


def plan_online(org, result, cfg, lang="fa") -> str:
    gaps = "\n".join(f'- ({g["priority"]}) {g["question"]} [{g["answer"]}]' for g in result["gaps"]) or "- none"
    prompt = (
        f'Organization "{org or "unknown"}" was assessed for {result["title"]}: readiness {result["percent"]}% '
        f'(level: {result["level"]}). Gaps:\n{gaps}\n\n'
        f"Write a practical, prioritized, step-by-step action plan in {_lang_name(lang)} using Markdown (max 300 words)."
    )
    return _chat([{"role": "user", "content": prompt}], cfg, timeout=60)
