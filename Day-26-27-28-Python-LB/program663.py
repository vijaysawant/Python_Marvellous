# Replace charactor with underscroll (_)

def ReplaceChar(input):
    output = ""
    for ch in input:
        if ch == "a":
            output = output + '_'
        else:
            output = output + ch
    return output

def main():
    print("Enter string : ")
    str = input()

    iRet = ReplaceChar(str)
    print(f"Replace string is {iRet}")

if __name__ == "__main__":
    main()