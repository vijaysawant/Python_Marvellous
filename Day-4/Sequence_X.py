# This program is similar to Sequence.py , we are writing new function only CircleArea
PI = 3.14

def CircleArea(Radius):  
    Area = PI * Radius * Radius
    return Area

def main():
    radius = float(input("Enter radius of circle : "))
    
    Area = CircleArea(radius)
    print("Area of Circle is : ",Area)

if __name__ == "__main__":
    main()