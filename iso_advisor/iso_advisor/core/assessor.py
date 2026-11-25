"""ارزیابی آمادگی (Gap Analysis) و امتیازدهی (دوزبانه)."""
from .i18n import ans_label, t

ANSWERS = {"خیر": 0, "نسبی": 50, "بله": 100}  # کلیدهای داخلی ثابت؛ نمایش با ترجمه
LEVEL_LIMITS = [25, 50, 75, 90, 101]


def level_of(percent: float, lang: str = "fa") -> str:
    for i, limit in enumerate(LEVEL_LIMITS):
        if percent < limit:
            return t(lang, f"lv{i}")
    return t(lang, "lv4")


def evaluate(std: dict, answers: list[str], lang: str = "fa") -> dict:
    qs = std["questions"]
    if len(answers) != len(qs):
        raise ValueError("answers/questions length mismatch")
    values = [ANSWERS[a] for a in answers]
    percent = round(sum(values) / len(values), 1)
    gaps = [
        {"question": q, "answer": ans_label(a, lang), "high": a == "خیر",
         "priority": t(lang, "p_high" if a == "خیر" else "p_mid")}
        for q, a in zip(qs, answers) if a != "بله"
    ]
    gaps.sort(key=lambda g: not g["high"])
    return {
        "standard_id": std["id"],
        "title": f'{std["id"]} - {std.get("title", std.get("title_fa"))}',
        "percent": percent,
        "level": level_of(percent, lang),
        "lang": lang,
        "answers": [{"question": q, "answer": ans_label(a, lang), "score": v} for q, a, v in zip(qs, answers, values)],
        "gaps": gaps,
    }


def offline_plan(result: dict, lang: str | None = None) -> str:
    lang = lang or result.get("lang", "fa")
    if not result["gaps"]:
        return t(lang, "plan_done")
    lines = [t(lang, "plan_title", t=result["title"]), ""]
    for i, g in enumerate(result["gaps"], 1):
        verb = t(lang, "plan_no" if g["high"] else "plan_part")
        lines.append(f'{i}. ' + t(lang, "plan_item", p=g["priority"], v=verb, q=g["question"]))
    lines += ["", t(lang, "plan_tail")]
    return "\n".join(lines)
