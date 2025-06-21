"""
2. Write a class Rectangle with length and width. Add a method to compute area and perimeter.
Area: 50, Perimeter: 30
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def AreaOfRectangle(self):
        return (self.length * self.width)

    def PerimeterOFRectangle(self):
        return 2*(self.length + self.width)

def main():
    val1 = int(input("Enter length value: "))
    val2 = int(input("Enter width value: "))
    Obj1 = Rectangle(val1, val2)
    
    retVal = Obj1.AreaOfRectangle()
    print("Area of rectangle: ",retVal)

    retVal = Obj1.PerimeterOFRectangle()
    print("Perimeter of rectangle: ",retVal)

if __name__ == "__main__":
    main()