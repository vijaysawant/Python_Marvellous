# Find Factorial using recursive function

Fact = 1
def Factorial(num):
    global Fact
    if num >= 1:
        Fact = Fact * num
        num = num - 1
        Factorial(num)
    return Fact

def main():
    ret = Factorial(4)
    print("Factorial of 4 : ",ret)

if __name__ == "__main__":
    main()