# Ransomware-Analyzer

Ransomware-Analyzer is a Python-based tool that simulates ransomware behavior for cybersecurity learning, testing, and research in a controlled environment. It encrypts and decrypts files in a target directory, allowing researchers and learners to study ransomware mechanisms safely.

---

## ⚙️ Features

- Encrypts files in a specified folder using **Fernet symmetric encryption**.
- Supports **parallel encryption/decryption** using multithreading for efficiency.
- Fetches encryption keys via a **Telegram Bot** for secure key management.
- Provides an interactive **decryption prompt** for recovering files.
- Logs encryption/decryption events for tracking.
- Safe for testing in isolated environments only.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/AUX-441/Ransomware-Analyzer.git
cd Ransomware-Analyzer
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up a Telegram Bot:

* Create a bot using [BotFather](https://t.me/BotFather).
* Replace `BOT_TOKEN` in `Telegram_Bot.py` with your bot token.

---

## 📂 Usage

1. Set the target folder to test encryption:

```python
TARGET_FOLDER = r"D:\11"  # Change to your test folder
```

2. Run the main script:

```bash
python main.py
```

3. The script will:

* Wait for the encryption key from the Telegram Bot.
* Encrypt all files in the target folder.
* Optionally ask you to decrypt files using the key.

---

## 📌 File Structure

```
Ransomware-Analyzer/
│
├─ main.py                 # Main execution script
├─ Get_Key.py              # Handles key retrieval from Telegram Bot
├─ encrypted_code.py       # Encryption logic
├─ decrypted_code.py       # Decryption logic
├─ Telegram_Bot.py         # Telegram bot implementation for key generation
├─ logs/                   # Stores logs of encryption/decryption
├─ requirements.txt        # Python dependencies
└─ README.md
```

---

## 🔑 Telegram Bot Commands

* `/start` – Registers your chat ID to receive keys.
* `/getkey` – Generates and sends a new encryption key.

> **Note:** Never use this on production or personal files. This project is intended for **safe, controlled learning only**.

---

## 💡 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m "Add feature"`.
4. Push to your branch: `git push origin feature/YourFeature`.
5. Open a Pull Request with a clear description of your changes.

---

## ⚠️ Warning

* This tool **can encrypt real files**. Always test in a controlled environment.
* Do **not run on system-critical directories**.
* Use responsibly and ethically for educational purposes only.

---

## 📜 License

This project is for **educational use only**. See LICENSE for details.

```

This `README.md` fully documents your project with usage instructions, structure, and safety warnings.  

If you want, I can also create a **`CONTRIBUTING.md`** in Markdown and **a `requirements.txt`** for all the dependencies so the repo is immediately ready to run. Do you want me to do that next?
```
