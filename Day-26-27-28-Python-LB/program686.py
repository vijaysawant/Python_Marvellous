"""
Input Row: 5
Output:
* * * * *   0 spaces
 * * * *    1 spaces
  * * *     2 spaces
   * *      3 spaces
    *       4 spaces

"""


def Display(iRow):
    for i in range(iRow, 0, -1):
        print(" "*(iRow-i),end="")
        print("* "*i)
    print()

    
def main():
    iVal1 = int(input("Enter number of Rows : "))
    Display(iVal1)

if __name__ == "__main__":
    main()