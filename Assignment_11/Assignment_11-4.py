"""
4. Power function using Recursion.
Write a recursive function to calculate X^n

power(2,3) -> 8
"""

iRes = 1 
def power(iNum, iPower):
    global iRes
    if iPower:
        iRes = iRes * iNum
        iPower = iPower - 1
        power(iNum, iPower)
    return iRes


def main():
    iNum = int(input("Enter digit value : "))
    iPower = int(input("Enter power value : "))
    ret = power(iNum, iPower)
    print(f"{iNum} raise to {iPower} is {ret}")

if __name__ == "__main__":
    main()