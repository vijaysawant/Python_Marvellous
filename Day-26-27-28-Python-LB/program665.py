# Accept string from user and convert every occurance of small letters into upper case
# Note - small letters have greater ascii value and capital letters have greater ascii value

def StrUpr(input):
    output = ""
    for ch in input:
        if ch >= 'a' and ch <= 'z':
            output = output + (ch - 32)    # Error - TypeError: unsupported operand type(s) for -: 'str' and 'int'
        else:
            output = output + ch

def main():
    print("Enter string : ")
    str = input()

    iRet = StrUpr(str)
    print(f"Replace string is {iRet}")

if __name__ == "__main__":
    main()