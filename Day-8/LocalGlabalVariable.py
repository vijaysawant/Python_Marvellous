# Global variable - no is global variable
# Local variable - x and y are local variables

no = 11

def fun():
    print("--Inside fun--")
    x = 21
    print("Value of x is : ",x) # 21
    print("Value of no is : ",no)   # no 11

def sun():
    print("--Inside sun--")
    y = 51
    print("Value of y is : ",y) # y 51
    print("Value of no is : ",no)   # no 11

def main():
    fun()
    sun()

if __name__ == "__main__":
    main()