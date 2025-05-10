def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Result = Addition(Value1, Value2)
    print("Addition of 2 numbers : ",Result)

if __name__ == "__main__":
    main()