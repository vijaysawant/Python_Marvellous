import os

# addition of cube of number
def fun(no):
    sum = 0
    for i in range(1, no):
        sum = sum + (i*i*i)
    return sum

def main():
    ret = fun(9)
    print("Addition of cube of number : ",ret)

if __name__ == "__main__":
    main()