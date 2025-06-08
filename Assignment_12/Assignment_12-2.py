"""
2. WAP which contains one class named as CIrcle.
Circle class contains three instance variables as Radius, Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14
Inside init method initialise all instance variables to 0.0
There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display()
Accept() method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
And Display() method will display value of all the instance variables as Radius, Area, Circumference.
After designing the above class call all instance methods by creating multiple objects.
"""


class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self,radius):
        self.Radius = radius

    def CalculateArea(self):
        # Area = PI * radius * radius
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        # circumference = 2 * PI * radius
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius :",self.Radius)
        print("Area : ",self.Area)
        print("Circumference :",self.Circumference)


def main():
    obj = Circle()
    rad = 3
    obj.Accept(radius=rad)
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()