"""
4 . Write a program which display 5 times Marvellous on screen.
Output:     Marvellous
            Marvellous
            Marvellous
            Marvellous
            Marvellous
"""

def main():
    OutStr = "Marvellous"
    
    i = 0
    print("Print string using while loop")
    while i < 5:
        print(OutStr)
        i = i + 1
    
    print("\nPrint string using for loop")
    for _ in range(5):
        print(OutStr)

if __name__ == "__main__":
    main()

