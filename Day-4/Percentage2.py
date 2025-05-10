def CalculatePercentage(Total, Obtained):
    Percentage = ((Obtained / Total) * 100)
    return Percentage

def main():
    print("Enter total marks : ")
    value1 = int(input())

    print("Enter obtained marks : ")
    value2 = int(input())

    output = CalculatePercentage(value1, value2)

    print("Percentage is : ",output)

if __name__ == "__main__":
    main()
