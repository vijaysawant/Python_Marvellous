# Input 721 
# output :
# 1   2   7

def DisplayDigits(No):
    iDigit = 0
    while(No != 0):
        iDigit = No % 10
        No = No // 10
        print(iDigit, end="\t")

def main():
    print("Enter number : ")
    Value = int(input())
    DisplayDigits(Value)
    
if __name__ == "__main__":
    main()