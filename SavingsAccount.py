from Account import Account 
class SavingsAccount:
    def __init__(self, owner, balance=0.0, interest_rate=0.02):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate  # 2% by default

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"SavingsAccount(owner='{self.owner}', balance=${self.balance:.2f})"


