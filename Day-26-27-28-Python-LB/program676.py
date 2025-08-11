"""
Input Row: 5    Col: 4 
Output: 
*   *   *   *
*   *   *   *
*   *   *   *
*   *   *   *
*   *   *   *
"""


def Display(iRow, iCol):
    for _ in range(iRow):
        for _ in range(iCol):
            print("*", end="\t")
        print()
    print()

    # for i in range(1, iRow+1, 1):
    #     for j in range(1, iCol+1, 1):
    #         print("*", end="\t")
    #     print()
    # print()
    
def main():
    iVal1 = int(input("Enter number of Rows : "))
    iVal2 = int(input("Enter number of Columns : "))
    Display(iVal1, iVal2)

if __name__ == "__main__":
    main()