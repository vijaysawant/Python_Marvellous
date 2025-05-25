# Basics of OOP, Constructor, Destructor

class Arithematic:
    def __init__(self,A,B):
        print("--Inside Constructor--")
        self.No1 = A
        self.No2 = B

    def __del__(self):
        print("--Inside Destructor--")

    def Addition(self):
        Result = 0
        Result = self.No1 + self.No2
        return Result

def main():
    obj1 = Arithematic(10, 11)
    obj2 = Arithematic(20, 21)

    ret = obj1.Addition()
    print(ret)

    ret = obj2.Addition()
    print(ret)

if __name__ == "__main__":
    main()