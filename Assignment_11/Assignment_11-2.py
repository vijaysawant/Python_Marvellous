"""
2. Factorial Using Recursion
Write a recursive function to calculate factorial of a number.

factorial(5) -> 120
"""
Fact = 1
def findFactorial(inum):
    global Fact
    if inum:
        Fact = Fact * inum
        inum = inum - 1
        findFactorial(inum)
    return Fact

def main():
    iNum = int(input("Enter number : "))
    ret = findFactorial(iNum)
    print("Factorial is : ",ret)

if __name__ == "__main__":
    main()