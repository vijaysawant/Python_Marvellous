"""
5. Accept a number from the user and check whether it is prime or not.
Input: Enter a number: 11
Output: 11 is prime number.
"""

def CheckPrime(num):
    PrimeNum = None
    for i in range(1, num+1):
        if num % i == 0:
            # print("Prime : ", i)
            PrimeNum = True
        else:
            # print("Not Prime : ", i)
            PrimeNum = False
    return PrimeNum

def main():
    number = int(input("Enter a number : "))
    result = CheckPrime(number)
    if result == True:
        print(f"{number} is Prime number")
    else:
        print(f"{number} is not Prime number")


if __name__ == "__main__":
    main()