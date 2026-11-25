"""ISO Advisor - سامانه هوشمند پیشنهاد و ارزیابی ISO (Streamlit) — فارسی/English، روشن/تیره."""
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from core import assessor, database, llm_online, mode_manager, recommender, report
from core.i18n import ans_label, sector_label, t

st.set_page_config(page_title="ISO Advisor", page_icon="📋", layout="wide")


def build_css(lang: str, dark: bool) -> str:
    v = (dict(bg="#12141f", fg="#e8e9f3", card="#1c1f33", border="#33375a", muted="#a5a8c8", input="#232743")
         if dark else dict(bg="#f6f5ff", fg="#1f2040", card="#ffffff", border="#e2dfff", muted="#5b5d80", input="#ffffff"))
    d = "rtl" if lang == "fa" else "ltr"
    a = "right" if lang == "fa" else "left"
    return f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
:root {{--bg:{v['bg']};--fg:{v['fg']};--card:{v['card']};--border:{v['border']};--muted:{v['muted']};--inp:{v['input']};}}
html, body, .stApp, button, input, textarea {{font-family:'Vazirmatn', Tahoma, 'Segoe UI', sans-serif !important;}}
.stApp {{background:var(--bg); color:var(--fg); direction:{d};}}
[data-testid="stHeader"] {{background:transparent;}}
[data-testid="stSidebar"] {{background:var(--card); border-{'left' if lang=='fa' else 'right'}:1px solid var(--border);}}
[data-testid="stSidebar"] * {{direction:{d};}}
.stApp p, .stApp li, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4,
[data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"] *, [data-testid="stRadio"] label *,
[data-testid="stMetric"] *, [data-testid="stCaptionContainer"], [data-baseweb="tab"] {{color:var(--fg) !important; text-align:{a};}}
code, pre {{direction:ltr; text-align:left;}}
.hero {{background:linear-gradient(135deg,#5b4fe0,#8e6bff 60%,#ff7eb3); border-radius:20px; padding:26px 30px; margin-bottom:18px; box-shadow:0 10px 28px rgba(91,79,224,.28);}}
.hero h1, .hero p, .hero span {{color:#fff !important; margin:0;}}
.hero h1 {{font-size:1.9rem; font-weight:700;}} .hero p {{margin-top:6px; opacity:.95;}}
.chip {{display:inline-block; background:rgba(255,255,255,.2); border-radius:999px; padding:3px 14px; margin:12px 0 0 8px; font-size:.85rem;}}
.stButton > button, .stDownloadButton > button {{border-radius:12px; font-weight:700; padding:.55rem 1.3rem; border:1px solid var(--border); background:var(--card); color:var(--fg);}}
.stButton > button[kind="primary"] {{border:0; color:#fff; background:linear-gradient(135deg,#5b4fe0,#8e6bff);}}
[data-baseweb="tab-list"] {{gap:6px; border-bottom:1px solid var(--border);}}
[data-baseweb="tab"] {{border-radius:12px 12px 0 0; padding:10px 18px;}}
[data-testid="stMetric"], [data-testid="stExpander"] {{background:var(--card); border:1px solid var(--border); border-radius:14px; padding:12px;}}
[data-testid="stExpander"] summary * {{color:var(--fg) !important;}}
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"] > div, textarea, input {{background:var(--inp) !important; color:var(--fg) !important; border-color:var(--border) !important;}}
[data-baseweb="popover"] *, ul[role="listbox"] * {{background:var(--card) !important; color:var(--fg) !important;}}
.ia-table {{width:100%; border-collapse:collapse; background:var(--card); border-radius:12px; overflow:hidden;}}
.ia-table th {{background:#6c5ce7; color:#fff; padding:8px 12px; text-align:{a} !important;}}
.ia-table td {{color:var(--fg); padding:8px 12px; border-top:1px solid var(--border); text-align:{a};}}
.block-container {{padding-bottom:80px;}}
.ia-footer {{position:fixed; left:0; right:0; bottom:0; z-index:1000; text-align:center; padding:9px 12px; font-size:.92rem;
  background:var(--card); color:var(--muted); border-top:1px solid var(--border); direction:{d};}}
#MainMenu, footer {{visibility:hidden;}}
</style>"""


def show_table(df: pd.DataFrame):
    st.markdown(df.to_html(index=False, classes="ia-table", border=0, escape=True), unsafe_allow_html=True)


@st.cache_data(ttl=30)
def net_status() -> bool:
    return mode_manager.internet_ok()


# ---------- نوار کناری ----------
with st.sidebar:
    lang_choice = st.radio("🌐 زبان / Language", ["فارسی", "English"], horizontal=True)
    lang = "fa" if lang_choice == "فارسی" else "en"
    dark = st.toggle(t(lang, "dark_toggle"))
    st.divider()
    st.header(t(lang, "settings"))
    mode_labels = {"auto": t(lang, "mode_auto"), "online": t(lang, "mode_online"), "offline": t(lang, "mode_offline")}
    pref = st.radio(t(lang, "mode"), list(mode_labels), format_func=mode_labels.get, help=t(lang, "mode_help"))
    with st.expander(t(lang, "api_exp")):
        default_cfg = llm_online.get_config()
        key = st.text_input("API Key", type="password", value=default_cfg["api_key"])
        base = st.text_input("Base URL", value=default_cfg["base_url"])
        model = st.text_input("Model", value=default_cfg["model"])
    cfg = llm_online.get_config(key, base, model)
    mode, mode_note = mode_manager.resolve_mode(pref, cfg, net_status() if pref != "offline" else False, lang)
    (st.success if mode == "online" else st.warning)(t(lang, "st_online" if mode == "online" else "st_offline") + mode_note)


def style_fig(fig):
    fig.update_layout(template="plotly_dark" if dark else "plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig


st.markdown(build_css(lang, dark), unsafe_allow_html=True)
st.markdown(
    f'<div class="hero"><h1>📋 {t(lang, "app_title")}</h1><p>{t(lang, "app_sub")}</p>'
    f'<span class="chip">{t(lang, "chip1")}</span><span class="chip">{t(lang, "chip2")}</span>'
    f'<span class="chip">{t(lang, "chip3")}</span></div>', unsafe_allow_html=True)

kb = recommender.load_kb(lang)
kb_by_id = {s["id"]: s for s in kb}
sectors = sorted({x for s in kb for x in s["sectors"]})
tab_rec, tab_eval, tab_hist, tab_about = st.tabs([t(lang, k) for k in ("tab_rec", "tab_eval", "tab_hist", "tab_about")])

# ---------- تب ۱: پیشنهاد ----------
with tab_rec:
    org = st.text_input(t(lang, "org_name"), key="org")
    sector = st.selectbox(t(lang, "sector"), [None] + sectors,
                          format_func=lambda s: t(lang, "sector_none") if s is None else sector_label(s, lang))
    desc = st.text_area(t(lang, "desc"), height=140, placeholder=t(lang, "desc_ph"))
    if st.button(t(lang, "btn_rec"), type="primary"):
        if not desc.strip() and not sector:
            st.warning(t(lang, "need_input"))
        else:
            with st.spinner(t(lang, "spin_rec")):
                st.session_state.rec = mode_manager.smart_recommend(desc, sector, mode, cfg, lang)
                st.session_state.sector = sector

    if "rec" in st.session_state:
        results, used, note = st.session_state.rec
        if note:
            st.warning(note)
        st.caption(f'{t(lang, "method")}: {t(lang, "m_ai" if used == "online" else "m_rules")}')
        if not results:
            st.info(t(lang, "no_results"))
        for r in results:
            st.progress(r["match_percent"] / 100, text=f'{r["title"]} — {t(lang, "match", p=r["match_percent"])}')
            with st.expander(t(lang, "why")):
                for reason in r["reasons"]:
                    st.write("•", reason)
        if results:
            fig = go.Figure(go.Bar(x=[r["match_percent"] for r in results], y=[r["title"] for r in results],
                                   orientation="h", marker_color="#6c5ce7"))
            fig.update_layout(height=250 + 30 * len(results), xaxis_title=t(lang, "chart_x"), yaxis=dict(autorange="reversed"))
            st.plotly_chart(style_fig(fig), width="stretch")

# ---------- تب ۲: ارزیابی ----------
with tab_eval:
    ids = [s["id"] for s in kb]
    top = st.session_state.get("rec", ([], "", ""))[0]
    default_idx = ids.index(top[0]["id"]) if top and top[0]["id"] in ids else 0
    sid = st.selectbox(t(lang, "std_eval"), ids, index=default_idx, format_func=lambda i: f'{i} - {kb_by_id[i]["title"]}')
    std = kb_by_id[sid]
    st.write(t(lang, "eval_help"))
    answers = [st.radio(f"{i}. {q}", list(assessor.ANSWERS), horizontal=True, key=f"{sid}_{i}",
                        format_func=lambda a: ans_label(a, lang))
               for i, q in enumerate(std["questions"], 1)]
    if st.button(t(lang, "btn_eval"), type="primary"):
        result = assessor.evaluate(std, answers, lang)
        with st.spinner(t(lang, "spin_plan")):
            plan, used, note = mode_manager.smart_plan(st.session_state.get("org", ""), result, mode, cfg, lang)
        database.save(st.session_state.get("org", ""), st.session_state.get("sector"), result, plan, used)
        st.session_state.result = (result, plan, used, note)

    if "result" in st.session_state:
        result, plan, used, note = st.session_state.result
        st.divider()
        c1, c2 = st.columns([1, 2])
        with c1:
            g = go.Figure(go.Indicator(mode="gauge+number", value=result["percent"], number={"suffix": "%"},
                                       gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#6c5ce7"}}))
            g.update_layout(height=250, margin=dict(t=30, b=0))
            st.plotly_chart(style_fig(g), width="stretch")
            st.metric(t(lang, "maturity"), result["level"])
        with c2:
            st.subheader(result["title"])
            show_table(pd.DataFrame(result["answers"]).rename(
                columns={"question": t(lang, "col_q"), "answer": t(lang, "col_a"), "score": t(lang, "col_s")}))
        if note:
            st.warning(note)
        st.subheader(t(lang, "action_plan"))
        st.markdown(plan)
        d1, d2 = st.columns(2)
        d1.download_button(t(lang, "dl_html"), report.to_html(st.session_state.get("org", ""), result, plan, used, lang),
                           file_name="iso_report.html", mime="text/html")
        d2.download_button(t(lang, "dl_csv"), report.to_csv(result, lang), file_name="iso_report.csv", mime="text/csv")

# ---------- تب ۳: تاریخچه ----------
with tab_hist:
    rows = database.list_all()
    if not rows:
        st.info(t(lang, "hist_empty"))
    else:
        df = pd.DataFrame(rows)[["created", "org", "standard_id", "percent", "level", "mode"]]
        show_table(df.rename(columns={"created": t(lang, "h_date"), "org": t(lang, "h_org"), "standard_id": t(lang, "h_std"),
                                      "percent": t(lang, "h_score"), "level": t(lang, "h_level"), "mode": t(lang, "h_mode")}))
        sel = st.selectbox(t(lang, "trend"), sorted(df["standard_id"].unique()))
        sub = df[df["standard_id"] == sel].sort_values("created")
        f = go.Figure(go.Scatter(x=sub["created"], y=sub["percent"], mode="lines+markers", line=dict(color="#6c5ce7")))
        f.update_layout(yaxis=dict(range=[0, 100], title=t(lang, "trend_y")), height=300)
        st.plotly_chart(style_fig(f), width="stretch")
        if st.button(t(lang, "clear")):
            database.clear()
            st.rerun()

# ---------- تب ۴: درباره / ISO 25010 ----------
ABOUT = {
    "fa": [["تناسب عملکردی", "پیشنهاد استاندارد، ارزیابی آمادگی، نقشه‌ی اقدام و گزارش"],
           ["کارایی", "حالت آفلاین بدون تأخیر شبکه؛ نتایج در کمتر از یک ثانیه"],
           ["سازگاری", "اجرا روی ویندوز، مک و لینوکس؛ هر API سازگار با OpenAI"],
           ["قابلیت استفاده", "رابط دوزبانه، حالت روشن/تیره، پرسشنامه‌ی سه‌گزینه‌ای، نمودار"],
           ["قابلیت اطمینان", "بازگشت خودکار به آفلاین هنگام قطع اینترنت یا خطای API"],
           ["امنیت", "کلید API در حافظه‌ی نشست/متغیر محیطی؛ داده‌ها فقط محلی ذخیره می‌شوند"],
           ["قابلیت نگهداری", "معماری ماژولار، پایگاه دانش JSON جدا از کد، تست‌های واحد"],
           ["قابلیت حمل", "نصب با requirements.txt و فایل run.bat"]],
    "en": [["Functional suitability", "Standard recommendation, readiness assessment, action plan and report"],
           ["Performance efficiency", "Offline mode has no network latency; results in under a second"],
           ["Compatibility", "Runs on Windows, macOS and Linux; any OpenAI-compatible API"],
           ["Usability", "Bilingual UI, light/dark mode, three-option questionnaire, charts"],
           ["Reliability", "Automatic fallback to offline on network loss or API errors"],
           ["Security", "API key kept in session memory/env variable; data stored locally only"],
           ["Maintainability", "Modular architecture, JSON knowledge base separate from code, unit tests"],
           ["Portability", "Install via requirements.txt and run.bat"]],
}
with tab_about:
    st.subheader(t(lang, "about_title"))
    show_table(pd.DataFrame(ABOUT[lang], columns=[t(lang, "ab_c1"), t(lang, "ab_c2")]))
    st.caption(t(lang, "about_cap"))

# ---------- پانویس (در همه‌ی صفحه‌ها) ----------
st.markdown(f'<div class="ia-footer">{t(lang, "footer")}</div>', unsafe_allow_html=True)
