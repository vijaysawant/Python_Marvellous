"""
Input Row: 5    Col: 5
Output: 
* * * * *
*       *
*       *
*       *
* * * * *

"""


def Display(iRow, iCol):
    if iRow != iCol:
        print("Invalid Input")
        return

    for i in range(1, iRow+1, 1):
        for j in range(1, iCol+1, 1):
            if (i == 1) or (i == iRow) or (j == 1) or (j == iCol):
                print("*", end="\t")
            else:
                print(" ", end="\t")
        print()
    print()


    
def main():
    iVal1 = int(input("Enter number of Rows : "))
    iVal2 = int(input("Enter number of Columns : "))
    Display(iVal1, iVal2)

if __name__ == "__main__":
    main()