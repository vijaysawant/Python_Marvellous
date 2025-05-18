# Global variable - no is global variable
# Local variable - no is also local variable at line 6

no = 11

def fun(no):
    print("fun no :", no)   # 21

def main():
    print("main no :", no)  # 11
    fun(21)

if __name__ == "__main__":
    main()