from bankaccount import BankAccount

class User:		
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        self.accounts = {"savings": BankAccount(0.02)}

    def display_info(self):
        attrs = vars(self)
        for item in attrs.items():
            print(f'{item[0]}: {item[1]}')
        print("")
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return True
    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print("Insufficient points")
            return False
        self.gold_card_points -= amount
        return True
    def make_deposit(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self
    def make_withdrawal(self, account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self
    def display_user_balance(self, account_name):
        self.accounts[account_name].display_account_info()
        return self
    def add_account(self, account_name):
        if account_name in self.accounts:
            print("Account already exists with that name.")
            return self
        self.accounts[account_name] = BankAccount(0.02)
        return self
    def remove_account(self, account_name):
        if account_name not in self.accounts:
            print("Account does not exists with that name.")
            return self
        self.accounts.pop(account_name)
        return self
    def display_account_names(self):
        for account in self.accounts.keys():
            print(account)
        return self
    ### Could have just passed an instance of the other users account.
    def transfer_money(self, from_account_name, amount, other_user, to_account_name):
        if from_account_name not in self.accounts:
            print(f"Account does not exists with that name for {self.last_name}, {self.first_name}")
            return self
        if to_account_name not in other_user.accounts:
            print(f"Account does not exists with that name for {other_user.last_name}, {other_user.first_name}")
            return self
        self.accounts[from_account_name].withdraw(amount)
        other_user.accounts[to_account_name].deposit(amount)
        return self

usr1 = User("Jim","Hoss","jh@mail.com",22)
usr1.display_user_balance("savings").make_deposit("savings", 100).display_user_balance("savings")

usr1.display_account_names()
usr1.add_account("checking").make_deposit("checking", 10000).display_user_balance("checking")
usr1.display_account_names()

usr2 = User("Jane","Dee","jd@llc.com",44)

usr1.display_user_balance("checking")
usr2.display_user_balance("savings")

usr1.transfer_money("checking", 800, usr2, "savings")

usr1.display_user_balance("checking")
usr2.display_user_balance("savings")
