"""
7. Area and Perimeter of Rectangle
Accept the length and width of a rectangle. Calculate and display the area and perimeter.

Input:
Enter length: 5
Enter width: 3

Output:
Area: 15
Perimeter: 16
"""

def main():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    # find area of rectangle
    area = length * width
    print("Area : ",area)

    # find perimeter of rectangle
    perimeter = 2 * (length + width)
    print("Perimeter : ",perimeter)


if __name__ == "__main__":
    main()