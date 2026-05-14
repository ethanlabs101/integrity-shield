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
4. Future scans compare current hashes against the saved snapshot
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
