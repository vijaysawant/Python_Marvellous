"""
Print thiangle pattern using Nested Loops
Output: 
*
* *
* * *
* * * *
"""

def main():
    num = int(input("Enter number : "))
    for iRow in range(1, num+1):
        for iCol in range(iRow):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    main()