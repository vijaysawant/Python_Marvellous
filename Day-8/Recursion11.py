# Find Factorial using recursive function

def Factorial(num):
    Fact = 1
    while num:
        Fact = Fact * num
        num = num - 1
    return Fact

def main():
    ret = Factorial(4)
    print("Factorial of 4 : ",ret)

if __name__ == "__main__":
    main()