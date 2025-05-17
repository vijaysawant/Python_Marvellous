
"""
9. WAP which accept number from user and return nummber of digits in that number.
Input: 5187934      Output: 7

"""

def CalculateTotalDigits(num):
    i = 0
    while num != 0:
        i = i + 1
        num = num // 10

    return i


def main():
    inputNum = int(input("Enter large digit : "))
    result = CalculateTotalDigits(inputNum)
    print(f"Number of digits in {inputNum} : {result}")

if __name__ == "__main__":
    main()