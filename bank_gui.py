import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QComboBox, QMessageBox, QTextEdit
)
from models import BankAccount, SavingsAccount


class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank GUI")
        self.setGeometry(400, 200, 450, 500)

        self.account = None  # Current account object

        # ---------------- Account Creation Widgets ----------------
        self.owner_label = QLabel("Account Owner:")
        self.owner_input = QLineEdit()

        self.balance_label = QLabel("Starting Balance:")
        self.balance_input = QLineEdit()

        self.type_label = QLabel("Account Type:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Bank", "Savings"])
        self.type_combo.currentTextChanged.connect(self.toggle_interest_field)

        self.interest_label = QLabel("Interest Rate:")
        self.interest_input = QLineEdit()
        self.interest_label.hide()
        self.interest_input.hide()

        self.create_btn = QPushButton("Create Account")
        self.create_btn.clicked.connect(self.create_account)

        # ---------------- After Account Creation Widgets ----------------
        self.balance_display = QLabel("Current Balance: $0.00")
        self.balance_display.hide()

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.hide()

        self.deposit_btn = QPushButton("Deposit")
        self.deposit_btn.hide()
        self.deposit_btn.clicked.connect(self.deposit)

        self.withdraw_btn = QPushButton("Withdraw")
        self.withdraw_btn.hide()
        self.withdraw_btn.clicked.connect(self.withdraw)

        self.interest_btn = QPushButton("Apply Interest")
        self.interest_btn.hide()
        self.interest_btn.clicked.connect(self.apply_interest)

        # Transaction History
        self.history_label = QLabel("Transaction History:")
        self.history_label.hide()

        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.history.hide()

        # ---------------- Layout ----------------
        layout = QVBoxLayout()
        # Account creation section
        layout.addWidget(self.owner_label)
        layout.addWidget(self.owner_input)
        layout.addWidget(self.balance_label)
        layout.addWidget(self.balance_input)
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_combo)
        layout.addWidget(self.interest_label)
        layout.addWidget(self.interest_input)
        layout.addWidget(self.create_btn)

        # After account creation section
        layout.addWidget(self.balance_display)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.deposit_btn)
        layout.addWidget(self.withdraw_btn)
        layout.addWidget(self.interest_btn)
        layout.addWidget(self.history_label)
        layout.addWidget(self.history)

        self.setLayout(layout)

    # ---------------- Helper Functions ----------------
    def toggle_interest_field(self, text):
        """Show/Hide interest input for Savings account"""
        if text == "Savings":
            self.interest_label.show()
            self.interest_input.show()
        else:
            self.interest_label.hide()
            self.interest_input.hide()

    def create_account(self):
        """Create Bank or Savings Account"""
        owner = self.owner_input.text()
        try:
            balance = float(self.balance_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid balance amount!")
            return

        acc_type = self.type_combo.currentText()
        if acc_type == "Savings":
            try:
                rate = float(self.interest_input.text())
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid interest rate!")
                return
            self.account = SavingsAccount(owner, balance, rate)
            self.interest_btn.show()
        else:
            self.account = BankAccount(owner, balance)

        # Hide account creation fields
        self.owner_label.hide()
        self.owner_input.hide()
        self.balance_label.hide()
        self.balance_input.hide()
        self.type_label.hide()
        self.type_combo.hide()
        self.interest_label.hide()
        self.interest_input.hide()
        self.create_btn.hide()

        # Show transaction section
        self.balance_display.show()
        self.amount_input.show()
        self.deposit_btn.show()
        self.withdraw_btn.show()
        self.history_label.show()
        self.history.show()

        # Update balance display and history
        self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
        self.log_history(f"Account created for {owner} with balance ${balance:.2f}")
        QMessageBox.information(self, "Success", f"Account created for {owner}!")

    def deposit(self):
        try:
            amount = float(self.amount_input.text())
            if self.account.deposit(amount):
                self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
                self.log_history(f"Deposited: ${amount:.2f}")
            else:
                QMessageBox.warning(self, "Error", "Invalid deposit amount!")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount!")

    def withdraw(self):
        try:
            amount = float(self.amount_input.text())
            success = self.account.withdraw(amount)
            if success:
                self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
                self.log_history(f"Withdrawn: ${amount:.2f}")
            else:
                QMessageBox.warning(self, "Error", "Insufficient balance or minimum $50 required!")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount!")

    def apply_interest(self):
        if isinstance(self.account, SavingsAccount):
            self.account.apply_interest()
            self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
            self.log_history("Interest Applied")
        else:
            QMessageBox.warning(self, "Error", "Interest applies only to Savings Account!")

    def log_history(self, message):
        """Add message to transaction history"""
        self.history.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.show()
    app.exec_()
