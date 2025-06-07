"""
1. Print Numbers using Recurssion
Write a recursive function to print numbers from 1 to N.

Expected Output (for n = 5):
1 2 3 4 5
"""
iCnt = 1
def printNum(iNum):
    global iCnt
    while iCnt <= iNum:
        print(iCnt,end=" ")
        iCnt = iCnt + 1
        printNum(iNum)

def main():
    iNum = int(input("Enter number : "))
    printNum(iNum)
    print()
if __name__ == "__main__":
    main()