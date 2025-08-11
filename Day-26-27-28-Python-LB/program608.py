def Addition(No1, No2):
    Sum = 0
    Sum = No1 + No2
    return Sum

def main():
    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    Ans = 0
    Ans = Addition(value1, value2)
    print(f"Addition of {value1} and {value2} : {Ans}")

if __name__ == "__main__":
    main()