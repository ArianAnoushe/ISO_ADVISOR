# ISO Advisor — سامانه هوشمند پیشنهاد و ارزیابی ISO

## اجرا روی ویندوز (ساده‌ترین راه)
1. پایتون ۳.۱۰ یا بالاتر را نصب کنید (تیک Add python.exe to PATH را بزنید).
2. روی فایل `run.bat` دابل‌کلیک کنید. بار اول کتابخانه‌ها نصب می‌شوند و برنامه در مرورگر باز می‌شود.

## اجرای دستی
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## حالت آنلاین
کلید API را در نوار کناری برنامه وارد کنید، یا قبل از اجرا: `set XAI_API_KEY=کلید-شما`
(پیش‌فرض Grok از xAI؛ هر API سازگار با OpenAI با تغییر Base URL و Model کار می‌کند.)
اگر اینترنت یا کلید نباشد، برنامه خودکار آفلاین کار می‌کند.

## نصب بدون اینترنت
```
pip download -r requirements.txt -d wheels            (روی سیستم دارای اینترنت)
pip install --no-index --find-links wheels -r requirements.txt   (روی سیستم مقصد)
```

## تست
```
python -m unittest discover -s tests -v
```

## افزودن استاندارد جدید
یک عضو جدید به `data/standards.json` اضافه کنید (id، عنوان، حوزه‌ها، کلمات کلیدی، سؤال‌ها).

## زبان و تم
در نوار کناری می‌توانید بین فارسی/English و حالت روشن/تیره جابه‌جا شوید. پانویس «نوشته شده با ❤️ و ☕ توسط آرین و آرتینا» در همه‌ی صفحه‌ها و گزارش‌ها دیده می‌شود (متن در `core/i18n.py`، کلید `footer`).
