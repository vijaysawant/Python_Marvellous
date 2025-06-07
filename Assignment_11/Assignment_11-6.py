"""
6. Sum of First N Natural Numbers
Write a recursive function to calculate sum from 1 to n.

sum_n(5) -> 15
"""
iSum = 0
def sum_n(iNum):
    global iSum
    if iNum:
        iSum = iSum + iNum
        sum_n(iNum-1)
    return iSum

def main():
    retVal = 0
    retVal = sum_n(5)
    print("Sum of first 5 natural numbers : ",retVal)

if __name__ == "__main__":
    main()