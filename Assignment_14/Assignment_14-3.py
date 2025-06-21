"""
3. Create a class Book with private attribute __price. Add methods to get and set the price. Show encapsulation.
"""

class Book:
    def __init__(self):
        self.__price = 0

    def SetPrice(self, value):
        self.__price = value

    def GetPrice(self):
        return self.__price

def main():
    Obj = Book()
    print("Before setting value...")
    print("Book price value: ",Obj.GetPrice())
    Obj.SetPrice(value=100)
    print("After setting value...")
    print("Book price value: ",Obj.GetPrice())

if __name__ == "__main__":
    main()