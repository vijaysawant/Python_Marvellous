"""
Input Row: 4    Col: 4 
Output: 
$   *   *   *
*   $   *   *
*   *   $   *
*   *   *   $

"""


def Display(iRow, iCol):
    if iRow != iCol:
        print("Invalid Input")
        return

    for i in range(iRow):
        for j in range(iCol):
            if i == j:
                print("$",end="\t")
            else:
                print("*", end="\t")
        print()
    print()


    
def main():
    iVal1 = int(input("Enter number of Rows : "))
    iVal2 = int(input("Enter number of Columns : "))
    Display(iVal1, iVal2)

if __name__ == "__main__":
    main()