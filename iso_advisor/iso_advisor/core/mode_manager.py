"""انتخاب حالت آنلاین/آفلاین و بازگشت خودکار به آفلاین هنگام خطا."""
import socket

from . import assessor, llm_online, recommender
from .i18n import t


def internet_ok(timeout=2.0) -> bool:
    try:
        socket.create_connection(("1.1.1.1", 443), timeout=timeout).close()
        return True
    except OSError:
        return False


def resolve_mode(pref: str, cfg: dict, net_ok: bool | None = None, lang: str = "fa"):
    """pref: auto | online | offline (یا معادل فارسی) → (mode, note)"""
    if pref in ("offline", "آفلاین"):
        return "offline", t(lang, "n_offline_sel")
    net = internet_ok() if net_ok is None else net_ok
    if not cfg.get("api_key"):
        return "offline", t(lang, "n_nokey")
    if not net:
        return "offline", t(lang, "n_nonet")
    return "online", t(lang, "n_online")


def smart_recommend(description, sector, mode, cfg, lang="fa"):
    if mode == "online":
        try:
            return llm_online.recommend_online(description, sector, recommender.load_kb(lang), cfg, lang=lang), "online", ""
        except Exception as e:  # شبکه، کلید نامعتبر، پاسخ خراب ...
            return recommender.recommend(description, sector, lang=lang), "offline", t(lang, "n_err_rec", e=e)
    return recommender.recommend(description, sector, lang=lang), "offline", ""


def smart_plan(org, result, mode, cfg, lang="fa"):
    if mode == "online":
        try:
            return llm_online.plan_online(org, result, cfg, lang), "online", ""
        except Exception as e:
            return assessor.offline_plan(result, lang), "offline", t(lang, "n_err_plan", e=e)
    return assessor.offline_plan(result, lang), "offline", ""
