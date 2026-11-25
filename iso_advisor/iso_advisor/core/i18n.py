"""متن‌های دوزبانه (فارسی/انگلیسی)."""

STR = {
 "fa": {
  "app_title": "سامانه هوشمند پیشنهاد و ارزیابی ISO", "app_sub": "استاندارد مناسب را پیدا کنید و آمادگی سازمان‌تان را بسنجید",
  "chip1": "۸ استاندارد ISO", "chip2": "آنلاین + آفلاین", "chip3": "ارزیابی ISO/IEC 25010",
  "settings": "⚙️ تنظیمات", "dark_toggle": "🌙 حالت تیره", "mode": "حالت کار",
  "mode_help": "خودکار: اگر اینترنت و کلید API باشد آنلاین، وگرنه آفلاین.",
  "mode_auto": "خودکار", "mode_online": "آنلاین", "mode_offline": "آفلاین", "api_exp": "تنظیمات API (فقط حالت آنلاین)",
  "st_online": "🟢 آنلاین: ", "st_offline": "🟠 آفلاین: ",
  "n_offline_sel": "حالت آفلاین انتخاب شده است.", "n_nokey": "کلید API وارد نشده؛ حالت آفلاین فعال است.",
  "n_nonet": "اینترنت در دسترس نیست؛ به حالت آفلاین برگشتیم.", "n_online": "متصل به هوش مصنوعی (حالت آنلاین).",
  "n_err_rec": "خطای حالت آنلاین ({e})؛ نتیجه با حالت آفلاین ارائه شد.", "n_err_plan": "خطای حالت آنلاین ({e})؛ نقشه‌ی اقدام آفلاین نمایش داده شد.",
  "tab_rec": "۱. پیشنهاد استاندارد", "tab_eval": "۲. ارزیابی آمادگی", "tab_hist": "۳. تاریخچه", "tab_about": "۴. درباره‌ی سامانه",
  "org_name": "نام سازمان", "sector": "حوزه‌ی فعالیت", "sector_none": "(انتخاب نشده)", "desc": "شرح فعالیت و دغدغه‌های سازمان",
  "desc_ph": "مثلاً: شرکت نرم‌افزاری هستیم و نگران امنیت داده‌ی مشتریان و رضایت آن‌ها هستیم...",
  "btn_rec": "🔍 پیشنهاد استاندارد", "need_input": "حداقل یکی از «حوزه‌ی فعالیت» یا «شرح فعالیت» را وارد کنید.", "spin_rec": "در حال تحلیل...",
  "method": "روش تحلیل", "m_ai": "هوش مصنوعی (آنلاین)", "m_rules": "موتور قاعده‌محور (آفلاین)",
  "no_results": "استانداردی پیدا نشد. شرح دقیق‌تری وارد کنید یا حوزه‌ی فعالیت را انتخاب کنید.", "why": "چرا این پیشنهاد؟",
  "match": "تطابق {p}٪", "chart_x": "درصد تطابق", "std_eval": "استاندارد مورد ارزیابی",
  "eval_help": "به هر مورد پاسخ دهید: **خیر** (انجام نشده)، **نسبی** (ناقص یا در حال انجام)، **بله** (کامل).",
  "a_no": "خیر", "a_part": "نسبی", "a_yes": "بله", "btn_eval": "📊 محاسبه‌ی نتیجه", "spin_plan": "در حال ساخت نقشه‌ی اقدام...",
  "maturity": "سطح بلوغ", "col_q": "سؤال", "col_a": "پاسخ", "col_s": "امتیاز", "action_plan": "🛠 نقشه‌ی اقدام",
  "dl_html": "⬇️ گزارش HTML", "dl_csv": "⬇️ خروجی CSV", "hist_empty": "هنوز ارزیابی‌ای ذخیره نشده است.",
  "h_date": "تاریخ", "h_org": "سازمان", "h_std": "استاندارد", "h_score": "امتیاز", "h_level": "سطح", "h_mode": "حالت",
  "trend": "روند پیشرفت برای استاندارد", "trend_y": "امتیاز آمادگی (٪)", "clear": "🗑 پاک کردن تاریخچه",
  "about_title": "ارزیابی کیفیت خود سامانه بر اساس ISO/IEC 25010", "ab_c1": "ویژگی کیفی", "ab_c2": "پیاده‌سازی در این سامانه",
  "about_cap": "افزودن استاندارد جدید: فقط یک عضو به data/standards.json اضافه کنید؛ نیازی به تغییر کد نیست.",
  "footer": "نوشته شده با ❤️ و ☕ توسط آرین و آرتینا",
  "r_kw": "کلمه‌ی کلیدی «{kw}» در توضیحات شما", "r_sector": "مناسب حوزه‌ی «{s}»", "r_univ": "استاندارد عمومی قابل‌استفاده برای اغلب سازمان‌ها",
  "lv0": "اولیه", "lv1": "در حال توسعه", "lv2": "تعریف‌شده", "lv3": "مدیریت‌شده", "lv4": "آماده‌ی ممیزی",
  "p_high": "بالا", "p_mid": "متوسط", "plan_title": "### نقشه‌ی اقدام برای {t}", "plan_done": "همه‌ی موارد پوشش داده شده است. پیشنهاد می‌شود مدارک را برای ممیزی گواهی‌دهنده آماده کنید.",
  "plan_no": "راه‌اندازی و مستندسازی", "plan_part": "تکمیل و مستندسازی", "plan_item": "**[اولویت {p}]** {v}: {q}",
  "plan_tail": "پس از انجام اقدام‌ها، ارزیابی را دوباره اجرا و با تاریخچه مقایسه کنید.",
  "rep_title": "گزارش ارزیابی آمادگی ISO", "rep_org": "سازمان", "rep_std": "استاندارد", "rep_date": "تاریخ", "rep_mode": "حالت",
  "rep_level": "سطح", "rep_details": "جزئیات پاسخ‌ها", "rep_gaps": "شکاف‌ها", "rep_plan": "نقشه‌ی اقدام", "rep_nogaps": "شکافی وجود ندارد", "rep_unknown": "نامشخص",
  "csv_total": "امتیاز کل", "csv_level": "سطح",
 },
 "en": {
  "app_title": "ISO Smart Advisor", "app_sub": "Find the right standard and measure your organization's readiness",
  "chip1": "8 ISO standards", "chip2": "Online + Offline", "chip3": "ISO/IEC 25010 self-evaluation",
  "settings": "⚙️ Settings", "dark_toggle": "🌙 Dark mode", "mode": "Operating mode",
  "mode_help": "Auto: online if internet and an API key are available, otherwise offline.",
  "mode_auto": "Auto", "mode_online": "Online", "mode_offline": "Offline", "api_exp": "API settings (online mode only)",
  "st_online": "🟢 Online: ", "st_offline": "🟠 Offline: ",
  "n_offline_sel": "Offline mode selected.", "n_nokey": "No API key entered; offline mode is active.",
  "n_nonet": "No internet connection; switched to offline mode.", "n_online": "Connected to the AI service (online mode).",
  "n_err_rec": "Online mode error ({e}); results were produced in offline mode.", "n_err_plan": "Online mode error ({e}); showing the offline action plan.",
  "tab_rec": "1. Recommend", "tab_eval": "2. Readiness assessment", "tab_hist": "3. History", "tab_about": "4. About",
  "org_name": "Organization name", "sector": "Industry sector", "sector_none": "(not selected)", "desc": "Describe your activities and concerns",
  "desc_ph": "e.g. We are a software company worried about customer data security and satisfaction...",
  "btn_rec": "🔍 Recommend standards", "need_input": "Enter at least a sector or a description.", "spin_rec": "Analyzing...",
  "method": "Analysis method", "m_ai": "AI (online)", "m_rules": "Rule-based engine (offline)",
  "no_results": "No standard found. Enter a more detailed description or choose a sector.", "why": "Why this recommendation?",
  "match": "{p}% match", "chart_x": "Match percentage", "std_eval": "Standard to assess",
  "eval_help": "Answer each item: **No** (not done), **Partial** (incomplete or in progress), **Yes** (fully done).",
  "a_no": "No", "a_part": "Partial", "a_yes": "Yes", "btn_eval": "📊 Calculate result", "spin_plan": "Building the action plan...",
  "maturity": "Maturity level", "col_q": "Question", "col_a": "Answer", "col_s": "Score", "action_plan": "🛠 Action plan",
  "dl_html": "⬇️ HTML report", "dl_csv": "⬇️ CSV export", "hist_empty": "No assessments saved yet.",
  "h_date": "Date", "h_org": "Organization", "h_std": "Standard", "h_score": "Score", "h_level": "Level", "h_mode": "Mode",
  "trend": "Progress trend for standard", "trend_y": "Readiness score (%)", "clear": "🗑 Clear history",
  "about_title": "Self-evaluation of this system against ISO/IEC 25010", "ab_c1": "Quality characteristic", "ab_c2": "How this system addresses it",
  "about_cap": "To add a new standard, just add one entry to data/standards.json; no code change needed.",
  "footer": "Written with ❤️ and ☕ by Arian & Artina",
  "r_kw": "Keyword “{kw}” found in your description", "r_sector": "Suitable for the “{s}” sector", "r_univ": "General standard applicable to most organizations",
  "lv0": "Initial", "lv1": "Developing", "lv2": "Defined", "lv3": "Managed", "lv4": "Audit-ready",
  "p_high": "High", "p_mid": "Medium", "plan_title": "### Action plan for {t}", "plan_done": "Everything is covered. Prepare your documents for the certification audit.",
  "plan_no": "Set up and document", "plan_part": "Complete and document", "plan_item": "**[{p} priority]** {v}: {q}",
  "plan_tail": "After completing the actions, run the assessment again and compare it in History.",
  "rep_title": "ISO Readiness Assessment Report", "rep_org": "Organization", "rep_std": "Standard", "rep_date": "Date", "rep_mode": "Mode",
  "rep_level": "Level", "rep_details": "Answer details", "rep_gaps": "Gaps", "rep_plan": "Action plan", "rep_nogaps": "No gaps", "rep_unknown": "Unknown",
  "csv_total": "Total score", "csv_level": "Level",
 },
}

SECTORS_EN = {"تولیدی": "Manufacturing", "خدماتی": "Services", "آموزشی": "Education", "فناوری اطلاعات": "Information technology",
              "صنعتی": "Industrial", "ساختمانی": "Construction", "غذایی": "Food", "درمانی": "Healthcare", "مالی و بانکی": "Finance & banking"}
ANS_KEYS = {"خیر": "a_no", "نسبی": "a_part", "بله": "a_yes"}


def t(lang: str, key: str, **kw) -> str:
    s = STR.get(lang, STR["fa"])[key]
    return s.format(**kw) if kw else s


def sector_label(sector: str, lang: str) -> str:
    return SECTORS_EN.get(sector, sector) if lang == "en" else sector


def ans_label(answer_fa: str, lang: str) -> str:
    return t(lang, ANS_KEYS[answer_fa])
