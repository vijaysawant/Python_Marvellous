"""
4. Accept a number and print its factorial using a for loop.
Input: Enter a number : 5
Output: Factorial of 5 is : 120
"""
# Formula -  n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

def FindFactorial(number):
    Fact = 1
    for i in range(number):
        Fact = Fact * (i+1)
    return Fact

def main():
    number = int(input("Enter a number : "))
    result = FindFactorial(number)
    print(f"Factorial of {number} is :",result)

if __name__ == "__main__":
    main()