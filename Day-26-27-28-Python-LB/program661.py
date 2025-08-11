# Count small characters

def CountSmallChars(input):
    iCount = 0
    for ch in input:
        if ch >= "a" and ch <= "z":
            iCount += 1
    return iCount

def main():
    print("Enter string : ")
    str = input()

    iRet = CountSmallChars(str)
    print(f"Number of small letters in {str} are {iRet}")

if __name__ == "__main__":
    main()