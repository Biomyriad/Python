class BankAccount:
    bank_accounts = []
    def __init__(self, int_rate, balance=0):
        BankAccount.bank_accounts.append(self)
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            accrued_int = self.balance * self.int_rate
            self.balance += accrued_int
        return self
    @classmethod
    def display_all_accounts(cls):
        for account in cls.bank_accounts:
            account.display_account_info()