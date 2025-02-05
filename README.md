
# Checker Trakteer 🔍
![CMD Output Thumbnail](https://raw.githubusercontent.com/ajayalf/checker_trakteer/refs/heads/main/CMD.png)

## Validate Account Trakteer ✅ 
**Checker Trakteer** is a Python-based account validation tool for **Trakteer**, designed for efficiency and ease of use. It automatically checks account validity, handles CAPTCHA challenges, and generates detailed logs—all while providing real-time feedback in your terminal.

---

## Table of Contents 📑
- [Features](#features-)
- [Tested On](#tested-on-)
- [Installation & Usage](#installation--usage-)
  - [Log Files](#log-files-)
- [Disclaimer](#disclaimer-)

---

## Features ✨
- ✅ **Automated Dependency Installation** – Installs required Python modules with zero manual setup.
- 📊 **Real-Time Feedback** – Live updates in the CMD with color-coded status messages.
- ⏳ **Smart CAPTCHA Handling** – Automatic cooldowns and retries to bypass CAPTCHA blocks.
- 📁 **Robust Logging System** – Saves results in timestamped files for easy tracking.
  - `result_YYYYMMDD_HHMMSS.txt` – Full validation log.
  - `valid_YYYYMMDD_HHMMSS.txt` – List of working accounts.
  - `invalid_YYYYMMDD_HHMMSS.txt` – List of non-working accounts.

---

## Tested On 🔧
- ✅ **Python 3.12.3** (Compatible with Python 3.12+)

---

## Installation & Usage 🛠️

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ajayalf/checker_trakteer.git
cd checker_trakteer
```

### 2️⃣ Prepare Account List
Update the provided acc.txt file in the project root with your account credentials in the following format:
```txt
email@example.com:password
another_user@domain.com:12345
```

### 3️⃣ Run the Tool
```bash
python checker.py
```
- The script will **auto-install dependencies** if missing.
- Follow the on-screen prompts to start validation.

### Log Files 📂
Results are saved in three timestamped files:
- 🟢 **Valid Accounts**: `valid_YYYYMMDD_HHMMSS.txt`
- 🔴 **Invalid Accounts**: `invalid_YYYYMMDD_HHMMSS.txt`
- 📄 **Full Process Log**: `result_YYYYMMDD_HHMMSS.txt`

---

## Disclaimer ⚠️  
This tool is provided strictly for **educational purposes only**. By using this tool, you acknowledge that you are solely responsible for your actions and any consequences that may arise. The author assumes **no liability** for any direct, indirect, or consequential damages or violations of any terms of service resulting from its use.  

⚠️ **Use this tool responsibly and in compliance with all applicable laws and regulations.**  
⚠️ **Only use your own account—do not use this tool with accounts that do not belong to you.**  


---
