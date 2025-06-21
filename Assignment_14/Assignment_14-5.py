"""
5. Create a class BankAccount with account_number, name, and balance. 
Use __init__ and create methods for deposit, withdraw, and displaying balance.
"""

class BankAccount:
    COUNT = 1
    def __init__(self):
        self.account_number = BankAccount.COUNT
        self.name = None
        self.account_balance = 0.0
    
    def create(self, account_name, account_balance):
        BankAccount.COUNT = BankAccount.COUNT + 1
        self.name = account_name
        self.account_balance = account_balance
    
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
    
    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
    
    def display_balance(self):
        print("Displaying account balance details")
        print("Account Number : ", self.account_number)
        print("Account Namme : ", self.name)
        print("Account Balance : ", self.account_balance)

def main():
    bank_obj = BankAccount()
    print("Creating Bank account")
    bank_obj.create(account_name="ABC company",account_balance=1000000.0)
    bank_obj.display_balance()
    print("Deposit 10000")
    bank_obj.deposit(amount=10000)
    bank_obj.display_balance()
    print("Withdraw 5000")
    bank_obj.withdraw(amount=5000)
    bank_obj.display_balance()
    print()
    bank_obj_1 = BankAccount()
    print("Creating Bank account")
    bank_obj_1.create(account_name="PQR Associates",account_balance=5000000.0)
    bank_obj_1.display_balance()
    print("Deposit 50000")
    bank_obj_1.deposit(amount=50000)
    bank_obj_1.display_balance()
    print("Withdraw 25000")
    bank_obj_1.withdraw(amount=25000)
    bank_obj_1.display_balance()

if __name__ == "__main__":
    main()