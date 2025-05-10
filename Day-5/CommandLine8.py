import sys
from CommandLineModule import Addition

def main():
    if(sys.argv[1] == '--h'):
        print("This application is use to perform addition of 2 numbers")
        return
    if(sys.argv[1] == '--u'):
        print("Execute code as :")
        print("$ python filename.py <interger-1> <interger-2>")
        return
    if len(sys.argv) != 3:
        print(f"Warning.. pass 2 integer arguments only, {len(sys.argv)-1} were given")
        print("You can use --h for help and --u for usage")
    else:
        Value1 = int(sys.argv[1])
        Value2 = int(sys.argv[2])

        Result = Addition(Value1, Value2)
        print("Addition of 2 numbers : ",Result)

if __name__ == "__main__":
    main()