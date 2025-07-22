import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QComboBox, QMessageBox
)
from models import BankAccount, SavingsAccount

class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank GUI")
        self.setGeometry(400, 200, 400, 400)

        self.account = None  # Current account object

        # Widgets
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

        self.balance_display = QLabel("Current Balance: $0.00")
        self.balance_display.hide()

        # Transaction widgets
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

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.owner_label)
        layout.addWidget(self.owner_input)
        layout.addWidget(self.balance_label)
        layout.addWidget(self.balance_input)
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_combo)
        layout.addWidget(self.interest_label)
        layout.addWidget(self.interest_input)
        layout.addWidget(self.create_btn)
        layout.addWidget(self.balance_display)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.deposit_btn)
        layout.addWidget(self.withdraw_btn)
        layout.addWidget(self.interest_btn)

        self.setLayout(layout)

    def toggle_interest_field(self, text):
        if text == "Savings":
            self.interest_label.show()
            self.interest_input.show()
        else:
            self.interest_label.hide()
            self.interest_input.hide()

    def create_account(self):
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

        # Show transaction widgets
        self.balance_display.show()
        self.deposit_btn.show()
        self.withdraw_btn.show()
        self.amount_input.show()

        self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
        QMessageBox.information(self, "Success", f"Account created for {owner}!")

    def deposit(self):
        if not self.account:
            QMessageBox.warning(self, "Error", "Create an account first!")
            return
        try:
            amount = float(self.amount_input.text())
            self.account.deposit(amount)
            self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount!")

    def withdraw(self):
        if not self.account:
            QMessageBox.warning(self, "Error", "Create an account first!")
            return
        try:
            amount = float(self.amount_input.text())
            success = self.account.withdraw(amount)
            if not success:
                QMessageBox.warning(self, "Error", "Insufficient balance or minimum limit!")
            else:
                self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount!")

    def apply_interest(self):
        if isinstance(self.account, SavingsAccount):
            self.account.apply_interest()
            self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
        else:
            QMessageBox.warning(self, "Error", "Interest applies only to Savings Account!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.show()
    app.exec_()
