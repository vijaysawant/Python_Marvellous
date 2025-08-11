# Count vowels

def CountVowels(input):
    iCount = 0
    for ch in input:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            iCount += 1
    return iCount

def main():
    print("Enter string : ")
    str = input()

    iRet = CountVowels(str)
    print(f"Number of vowels in {str} are {iRet}")

if __name__ == "__main__":
    main()