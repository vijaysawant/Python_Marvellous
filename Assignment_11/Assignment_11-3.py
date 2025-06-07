"""
3. Sum of Digits
Writa a recursive function to calculate the sum of digits of a number.

sum_of_digits(1234) -> 10
"""
sum = 0
def sum_of_digits(iNum):
    global sum
    if iNum:
        lastDigit = iNum % 10
        sum = sum + lastDigit
        sum_of_digits(iNum//10)
    return sum
    

def main():
    iNum = int(input("Enter number : "))
    ret = sum_of_digits(iNum)
    print("Sum of digits : ", ret)

if __name__ == "__main__":
    main()