"""
Input Row: 5
Output:

*
* *
* * *
* * * *
* * * * *
"""


def Display(iRow):
    for i in range(1, iRow+1, 1):
        print("*\t"*i)
    print()

    
def main():
    iVal1 = int(input("Enter number of Rows : "))
    Display(iVal1)

if __name__ == "__main__":
    main()