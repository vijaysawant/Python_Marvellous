"""
5. WAP which accept accept one number from user and check whether number is prime or not.
Input: 5        Output: It is Prime Number
"""
def CheckPrime(Num):
    IsPrime = True
    for i in range(2, Num):
        if Num % i  == 0:
            IsPrime = False
    return IsPrime


def main():
    num = int(input("Enter number : "))
    res = CheckPrime(num)
    if res == True:
        print("Number is prime")
    else:
        print("Number is not prime")
if __name__ == "__main__":
    main()