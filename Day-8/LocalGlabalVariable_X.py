# Global variable - no is global variable
# Local variable - x and y are local variables

no = 11

def fun():
    global no
    print("--Inside fun--")
    x = 21
    print("Value of x is : ",x) # 21
    no = no + 1
    print("Value of no is : ",no)   # no 12

def main():
    print("Value of no before fun : ",no)   # no => 11
    fun()
    print("Value of no after fun : ",no)    # no => 12

if __name__ == "__main__":
    main()