
def CountFrequency(input):
    iCount = 0
    for ch in input:
        if ch == 'a':
            iCount += 1
    return iCount

def main():
    print("Enter string : ")
    str = input()

    iRet = CountFrequency(str)
    print(f"Frequncy of a in {str} is {iRet}")

if __name__ == "__main__":
    main()