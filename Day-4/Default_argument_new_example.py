def CalculatePercentage(Obtained = 400, Total = 500):
    Percentage = ((Obtained / Total) * 100)
    return Percentage

def main():
    
    output = CalculatePercentage(350, 450)  # Default arguments
    print("Percentage is : ",output)

    output = CalculatePercentage(350)
    print("Percentage is : ",output)

    output = CalculatePercentage()
    print("Percentage is : ",output)

if __name__ == "__main__":
    main()
