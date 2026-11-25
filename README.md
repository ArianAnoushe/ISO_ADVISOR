# ISO ADVISOR

**An AI-Powered ISO Standards Advisor**

ISO ADVISOR is a Python-based university project designed to assist users with ISO-related information and standards analysis through an interactive interface.

The project aims to make working with ISO standards more accessible by providing an AI-assisted environment with support for multiple languages.

---

## Features

- **Bilingual Interface:** Supports both English and Persian.
- **Interactive UI:** Built with Streamlit.
- **AI-Assisted Analysis:** Designed to assist users with ISO-related information.
- **User-Friendly Experience:** Simple and accessible interface.
- **Expandable Architecture:** Designed to support future improvements and additional features.

## Supported Languages

Currently, ISO ADVISOR supports:

- English 🇬🇧
- Persian (فارسی) 🇮🇷

More languages may be added in future updates.

---

## Requirements

Before installing the project, make sure you have:

- Python 3.10 or higher
- pip (Python Package Installer)
- An internet connection
- Git (optional, depending on the installation method)

---

## Installation

There are several ways to download ISO ADVISOR.

### Option 1: Using Git (Recommended)

Make sure Git is installed, then open CMD, PowerShell, or Terminal and run:

```bash
git clone https://github.com/D5F8ULT/ISO_ADVISOR.git
cd ISO_ADVISOR
```

### Option 2: Download Without Git (PowerShell)

If you don't have Git installed, open PowerShell and run:

```powershell
Invoke-WebRequest -Uri "https://github.com/D5F8ULT/ISO_ADVISOR/archive/refs/heads/main.zip" -OutFile "ISO_ADVISOR.zip"

Expand-Archive -Path "ISO_ADVISOR.zip" -DestinationPath "."

cd ISO_ADVISOR-main
```

### Option 3: Download Using CMD

Open Command Prompt and run:

```cmd
curl -L -o ISO_ADVISOR.zip https://github.com/D5F8ULT/ISO_ADVISOR/archive/refs/heads/main.zip

tar -xf ISO_ADVISOR.zip

cd ISO_ADVISOR-main
```

### Option 4: Download Using Python

If Python is installed, you can download and extract the project using:

```bash
python -c "import urllib.request, zipfile; urllib.request.urlretrieve('https://github.com/D5F8ULT/ISO_ADVISOR/archive/refs/heads/main.zip', 'ISO_ADVISOR.zip'); zipfile.ZipFile('ISO_ADVISOR.zip').extractall('.')"
```

**Note:** The ZIP download commands assume that the default branch is named `main`.

---

## Install Dependencies

Navigate to the project directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

If you have multiple Python versions installed, you can use:

```bash
python -m pip install -r requirements.txt
```

---

## Running the Application

ISO ADVISOR uses Streamlit for its graphical user interface.

To launch the application, use:

```bash
streamlit run app.py
```

Streamlit will start a local web server and provide a URL, usually:

```text
http://localhost:8501
```

Open this address in your browser to access the application.

**Note:** Replace `app.py` with the actual Streamlit entry-point filename if your project uses a different filename.

---

## Technologies & Libraries

The project is developed using Python and Streamlit.

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive user interface |
| pip | Dependency management |

Additional libraries are listed in `requirements.txt`.

---

## Project Status

<code>Version: Initial Development</code>

ISO ADVISOR is currently an academic project under development. Its functionality, interface, and architecture are expected to improve over time.

---

## Creator's Note

ISO ADVISOR is currently a university project developed as an initial version of an AI-assisted ISO standards advisor.

At this stage, the project supports two languages: **English and Persian**.

This is only the beginning of the development process. The project is expected to undergo continuous improvements, including new features, enhanced functionality, interface refinements, and overall performance improvements.

Feedback, suggestions, and contributions are always welcome. <3 Arian

---

## Contributing

Contributions and suggestions are welcome!

If you have ideas for improving ISO ADVISOR, feel free to:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

---

## License

This project is currently an academic project.

License details may be added in future versions.

---

**Developed with Python ❤️**
