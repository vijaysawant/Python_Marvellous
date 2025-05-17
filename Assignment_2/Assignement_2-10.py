"""
10. WAP which accept number from user and returrn addition of digits in that number.
Input: 5187934      Output: 37

"""

def CalculateSumOfDigits(num):
    sum = 0
    while num != 0:
        sum = sum + (num % 10)
        num = num // 10
    return sum

def main():
    inputNum = int(input("Enter large digit : "))
    result = CalculateSumOfDigits(inputNum)
    print(f"Sum of digits {inputNum} : {result}")

if __name__ == "__main__":
    main()