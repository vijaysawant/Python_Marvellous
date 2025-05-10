def CalculatePercentage(Obtained, Total = 500):
    Percentage = ((Obtained / Total) * 100)
    return Percentage

def main():
    # print("Enter total marks : ")
    # value1 = int(input())

    print("Enter obtained marks : ")
    value2 = int(input())

    output = CalculatePercentage(value2)    # Default arguments - Here 'Total' is default argument

    print("Percentage is : ",output)

if __name__ == "__main__":
    main()
