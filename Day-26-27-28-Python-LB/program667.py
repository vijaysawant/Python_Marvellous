# Accept string from user and convert every occurance of small letters into upper case
# Note - small letters have greater ascii value and capital letters have greater ascii value

def StrUpr(input):
    output = ""
    for ch in input:
        if ch >= 'a' and ch <= 'z':
            # chr() convert ascii into char and ord() convert char into ascci
            output = output + chr(ord(ch) - 32)
        else:
            output = output + ch
    return output
def main():
    print("Enter string : ")
    str = input()

    iRet = StrUpr(str)
    print(f"Replace string is {iRet}")

if __name__ == "__main__":
    main()