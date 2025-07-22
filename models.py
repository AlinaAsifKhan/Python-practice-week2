# Step 1: Models - BankAccount and SavingsAccount

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = float(balance)  # Ensure numeric balance

    # Deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    # Withdraw amount (only if sufficient balance)
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)  # Call Parent __init__
        self.interest_rate = interest_rate

    # Overridden withdraw: Must maintain minimum $50 after withdrawal
    def withdraw(self, amount):
        if self.balance - amount >= 50:
            self.balance -= amount
            return True
        return False

    # Apply interest to balance
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
