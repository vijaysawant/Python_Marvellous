import sys
from CommandLineModule import Addition

def main():
    if len(sys.argv) != 3:
        print(f"Warning.. pass 2 integer arguments, {len(sys.argv)-1} were given")
    else:
        Value1 = int(sys.argv[1])
        Value2 = int(sys.argv[2])

        Result = Addition(Value1, Value2)
        print("Addition of 2 numbers : ",Result)

if __name__ == "__main__":
    main()