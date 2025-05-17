"""
2. Write a program which accept one numbner and display below pattern
Input: 5
Output: 
*   *   *   *   *
*   *   *   *   *  
*   *   *   *   *  
*   *   *   *   *  
*   *   *   *   *  
"""

def main():
    num = int(input("Accept number to print patter : "))
    if num <= 0:
        print("Number should be greater than 0")
        return
    for iRow in range(num):
        for iCol in range(num):
            print("*    ", end="")
        print("\n")

if __name__ == "__main__":
    main()