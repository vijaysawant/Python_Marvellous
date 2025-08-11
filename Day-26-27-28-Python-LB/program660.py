# Count non vowels

def CountVowels(input):
    iCount = 0
    pattern = "aeiouAEIOU"
    for ch in input:
        if ch not in pattern:
            iCount += 1
    return iCount

def main():
    print("Enter string : ")
    str = input()

    iRet = CountVowels(str)
    print(f"Number of non-vowels in {str} are {iRet}")

if __name__ == "__main__":
    main()