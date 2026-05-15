# Integrity Shield 🛡️

![Python](https://img.shields.io/badge/Python-EF1FFF?style=for-the-badge&logo=python&logoColor=white)

---
## ***Integrity Shield is a lightweight file integrity monitoring tool built in Python.*** 
## It scans directories, generates SHA-256 hashes for files/folders, and compares snapshots to detect changes such as modifications, new files, or missing files.
## Designed as a simple but practical introduction to filesystem security concepts, hashing, and CLI tool design.

---

![integrity-shield1](https://github.com/ethanlabs101/integrity-shield/blob/main/images/integrity-shield.png)

---

# 🚀 Features
- 📁 Recursive folder scanning
- 🔒 SHA-256 file hashing
- 📷 Snapshot creation and storage
- 🔍 Integrity verification against saved snapshots
- ⚠️ Detection of:
  - Modified Files
  - New Files
  - Missing Files
- 🖥️ Clean TUI
- 🧹 Auto-clear interface for smooth interaction
- 👤 User-safe storage using home directory config path

---

# 🧠 What I Learned Building This
## ***This project was built to strengthen my understanding of:***
  - Python file handling
  - Directory Transversal
  - Hashing Algorithms
  - CLI/TUI Structure and user flow design
  - Clean Architecture for small tools

---

# ⚙️ How It Works
1. The tool scans a target directory recursively
2. Each file is hashed using SHA-256
3. A snapshot is saved locally
4. Future scans compare current hashes against the saved snapshot to determine file(s) integrity
5. Differences are reported as:
   - New File
   - Modified
   - Missing

---

# 📦 Installation

1. Clone This Repo
```html
git clone https://github.com/ethanlabs101/integrity-shield.git
```
2. Run Script
```html
cd integrity-shield
python3 main.py
```

> Only Python and Git required to run. No extra external dependencies needed

---

# ▶️ Usage

1. Run the tool:
```html
python3 main.py
```

2. Then Choose Menu Option:
```html
[1] Save Snapshot
[2] Check Snapshot
[3] Exit
```
# 📸 Save Snapshot
- Enter target folder path
- Tool generates SHA-256 hashes
- Snapshot stored locally

# 🔍 Check Snapshot
- Enter the same folder path
- Tool compares current state vs saved snapshot
- Outputs any changes detected

---

# 📂 Snapshot Storage

## Snapshots are stored locally in:
```html
~/.integrity_shield_snapshot.json
```
This ensures:
- No permission issues
- Works across different systems/users
- Keeps project directory clean

---

# 📚 Tech Stack
- Python 3
- hashlib (SHA-256)
- os /pathlib
- json
- CLI-based UI (custom TUI)

---

# ⚠️ Notes

- Designed for user-space directory scanning (Non-system/protected files).
- Not intended as a full system-wide/large scale audit tool.
- Uses a single snapshot database.
- Saving a new snapshot overwrites the previous stored baseline (1 at a time).

---

## 📜 License

This project is open source and released under the MIT License. See [LICENSE](https://github.com/ethanlabs101/rofi-emulator-menu/blob/main/LICENSE) for details.

---

## 🌐 Contact

[![GitHub](https://img.shields.io/badge/GitHub-ethanlabs101-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ethanlabs101)
[![Email](https://img.shields.io/badge/Email-ProtonMail-blue?style=for-the-badge&logo=protonmail&logoColor=white)](mailto:ethanlabs101@proton.me)
[![Discord](https://img.shields.io/badge/Discord-Chat-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/1460827490762363001)
[![Instagram](https://img.shields.io/badge/Instagram-ethanlabs101-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ethanlabs101/)

---

