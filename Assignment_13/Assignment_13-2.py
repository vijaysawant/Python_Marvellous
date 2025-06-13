"""
WAP which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5
Inside init method initialise all name and amount variable by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateInterest().
Deposit() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateInterest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.
"""

class BankAccount:
    ROI = 10.5
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount
        self.Interest = 0

    def Display(self):
        print("Name of customer: ",self.Name)
        print("Available Balance: ",self.Amount)
        print("Interest on amount: ",self.CalculateInterest())

    def Deposit(self, deposit_amt):
        print("[log][+]Deposit Amount=",deposit_amt)
        self.Amount = self.Amount + deposit_amt

    def Withdraw(self, withdraw_amt):
        print("[log][-]Withdraw Amount=",withdraw_amt)
        self.Amount = self.Amount - withdraw_amt

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100

def main():
    print("-"*30)
    Customer1 = BankAccount("Akshay", 10000)
    Customer1.Display()
    Customer1.Deposit(deposit_amt=15000)
    Customer1.Display()

    print("-"*30)
    Customer2 = BankAccount("Rahul", 50000)
    Customer2.Display()
    Customer2.Withdraw(withdraw_amt=500)
    Customer2.Display()


if __name__ == "__main__":
    main()