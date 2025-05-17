"""
3. Write a program which accept one number from user and return its factorial.
Input:  5       Output: 120
"""

def factorial(Num):
    Answer = 1
    for i in range(Num, 0, -1):
        Answer = Answer * i
    return Answer

def main():
    Num = int(input("Enter number to calculate factorial : "))
    Result = factorial(Num)
    print(f"Factorial of {Num} : {Result}")

if __name__ == "__main__":
    main()
