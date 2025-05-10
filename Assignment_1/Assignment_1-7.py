"""
7. Write a program which contains one function that accept one number from user and returns true
if number is divisible by 5 otherwise return false.
Input : 8       Output : False
Input : 5       Output : True
"""

def IsDivideBy(Number, Denominator=5):
    if Number % Denominator == 0:
        print(f"{Number} is divisible by {Denominator}")
        return True
    else:
        print(f"{Number} is not divisible by {Denominator}")
        return False

def main():
    Num = int(input("Enter number : "))
    IsDivideBy(Num)

if __name__ == "__main__":
    main()