"""
Input Row: 5    Col: 4
Output: 
$ $ $ $
$ $ $ $
$ $ $ $
$ $ $ $
$ $ $ $

"""


def Display(iRow, iCol):
    
    for i in range(1, iRow+1, 1):
        print("$\t"*iCol)
    print()


    
def main():
    iVal1 = int(input("Enter number of Rows : "))
    iVal2 = int(input("Enter number of Columns : "))
    Display(iVal1, iVal2)

if __name__ == "__main__":
    main()