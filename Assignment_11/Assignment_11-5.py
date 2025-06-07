"""
5. Count Zeros in a Number (Recursively)
Write a recursive function to count how many zeros are in the given number.

Count_zeros(1020300) -> 4
"""

iCount = 0
def Count_zeros(iNum):
    global iCount
    lastDigit = None
    newNum = None
    if iNum:
        lastDigit = iNum % 10
        if lastDigit == 0:
            iCount = iCount + 1
        newNum = iNum // 10
        Count_zeros(newNum)
    return iCount

def main():
    retVal = 0
    retVal = Count_zeros(1020300)
    print("Total Zeros in the numbers : ",retVal)

if __name__ == "__main__":
    main()