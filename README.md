# 🏦 Bank Account GUI App (PyQt5)

A simple **Bank Account Management System** built with **Python and PyQt5**.  
It supports **BankAccount** and **SavingsAccount**, allowing deposits, withdrawals, interest application, and transaction history tracking.

---

## ✅ Features
- Create **Bank Account** or **Savings Account**.
- Show and update **balance live**.
- **Deposit** and **Withdraw** money with validation.
- **SavingsAccount** enforces minimum $50 after withdrawal.
- Apply **interest** (SavingsAccount only).
- **Transaction history log** for all actions.
- Simple, clean **GUI with PyQt5**.

---

## 🛠️ Requirements
- Python 3.x
- PyQt5

Install PyQt5:
```bash
pip install PyQt5
```

---

## ▶ Steps to Run
1. Clone the repo:
```bash
git clone https://github.com/AlinaAsifKhan/Python-practice-week2.git
```

2. Navigate to the project folder:
```bash
cd Python-practice-week2/Bank-project-gui
```

3. (Optional) Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

4. Run the GUI app:
```bash
python bank_gui.py
```

---

## 🖼️ How It Works
- Enter **Account Owner**, **Starting Balance**, choose **Account Type**.
- For **Savings Account**, enter **Interest Rate**.
- Click **Create Account** → Enables **Deposit**, **Withdraw**, **Apply Interest**.
- Use **Transaction Log** to view all actions.

---
