"""
3. WAP which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
ChkPrime() method will return ture if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.
"""
class Numbers:
    def __init__(self):
        self.IsPrime = None
        self.IsPerfect = None

    def ChkPrime(self, Num):
        self.IsPrime = True
        for i in range(2, Num):
            if Num % i  == 0:
                self.IsPrime = False
        return self.IsPrime

    def ChkPerfect(self,Num):
        sum = 0
        for i in range(1, (Num//2)+1):
            if Num % i == 0:
                sum = sum + i
        if sum == Num:
            self.IsPerfect = True
        else:
            self.IsPerfect = False
        return self.IsPerfect

    def SumFactors(self, Num):
        self.FactorSum = 0
        for i in range(1, (Num//2)+1):
            if Num % i == 0:
                # print(i)
                self.FactorSum = self.FactorSum + i
        return self.FactorSum

    def Factors(self, Num):
        for i in range(1, (Num//2)+1):
            if Num % i == 0:
                print(i)

def main():
    Obj = Numbers()
    Number = int(input("Enter number: "))
    if Obj.ChkPrime(Number):
        print(f"{Number} is Prime")
    else:
        print(f"{Number} is not Prime")
    print()

    if Obj.ChkPerfect(Number):
        print(f"{Number} is Perfect")
    else:
        print(f"{Number} is not Perfect")
    print()
    print(f"Sum of factors of {Number}: ",Obj.SumFactors(Number))
    print()
    Obj.Factors(Number)
    print(f"Are the Factors of {Number}",end="\n")


if __name__ == "__main__":
    main()