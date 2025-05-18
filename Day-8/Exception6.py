# Exception handling in python
# Divide by 0 exception

def main():
    Ans = 0
    try:
        print("Enter first number : ")
        no1 = int(input())

        print("Enter second number : ")
        no2 = int(input())

        Ans = no1 / no2
    
    except ZeroDivisionError as zobj:
        print("Exception occured due to second input : ",zobj)

    except ValueError as vobj:
        print("Exception occured due invalid data type of input : ",vobj)

    except Exception as eobj:
        print("Exception occured : ", eobj)

    finally:
        print("Inside finally block")
    print("Division is : ", Ans)


if __name__ == "__main__":
    main()