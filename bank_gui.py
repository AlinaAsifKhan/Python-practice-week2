import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
)
from models import BankAccount, SavingsAccount


class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank GUI")
        self.setGeometry(400, 200, 400, 300)

        # Current account object
        self.account = None

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
        else:
            self.account = BankAccount(owner, balance)

        self.balance_display.setText(f"Current Balance: ${self.account.balance:.2f}")
        QMessageBox.information(self, "Success", f"Account created for {owner}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.show()
    sys.exit(app.exec_())
