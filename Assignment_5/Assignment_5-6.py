"""
6. Celsius to Fahrenheit converter
Accept temperature in Celsius and convert it to Fahrenheit using the formula:
F = (c * 9/5) + 32

Input: Enter temperature in Celsius: 25
Output: Temperature in Fahrenheit: 77.0 F
"""


def main():
    fahrenheit = 0.0
    temp = int(input("Enter temperature in Celsius : "))
    fahrenheit = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit} F")


if __name__ == "__main__":
    main()