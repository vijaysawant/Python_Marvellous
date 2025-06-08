"""
1. WAP which contains one class named a Demo.
Demo class contains two instance variables as no1, no2.
That class contains one class variable as Value.
There are 2 instance methods of class variables as Fun and Gun which displays values of instance varibles.
Initialise instance variable in init method by accepting the values from user.

After creating the class create 2 objects of Demo class as 
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
"""

class Demo:
    value = 0
    def __init__(self,num1, num2):
        print("-- Inside constructor --")
        self.no1 = num1
        self.no2 = num2

    def Fun(self):
        print("-- Inside Fun --")
        print("Value of no1", self.no1)

    def Gun(self):
        print("-- Inside Gun --")
        print("Value of no2", self.no2)

def main():
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()