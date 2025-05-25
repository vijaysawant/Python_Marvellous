# Python is multiparadigm Procedural programming language

def Addition(A, B):
    result = 0
    result = A + B
    return result

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ret = Addition(No1, No2)
    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()