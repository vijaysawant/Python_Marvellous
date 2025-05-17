"""
4. Write a program whcih accept one number from user and return additon of its factors.
Input: 12       Output: 16  (1+2+3+4+6)
"""

def FactorAddition(Num):
    Result = 0
    for i in range(1, (Num//2)+1):
        if Num % i == 0:
            # print(i)
            Result = Result + i
    return Result

def main():
    Num = int(input("Enter number to calculate addition of factors : "))
    Result = FactorAddition(Num)
    print(f"Addition of factors for {Num} : {Result}")

if __name__ == "__main__":
    main()
