"""
7. Print Pattern Using recursiion (right triangel)
Write a recursive function to print the following pattern:

*
* *
* * *
* * * *
"""

"""
# Regular function
def patternRightTriangle(iCount):
    for r in range(iCount):
        for c in range(iCount):
            if c <= r:
                print("*",end=" ")
        print()
"""

iCount = 1
def patternRightTriangle(iNum):
    global iCount
    if iCount <= iNum:
        print("* "*iCount,end="\n")
        iCount = iCount + 1
        patternRightTriangle(iNum)

    return None
def main():
    patternRightTriangle(4)

if __name__ == "__main__":
    main()