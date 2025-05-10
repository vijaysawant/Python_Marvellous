"""
This program is to demonstrate CommandLine Argument concept.
"""
import sys

def main():
    print("Number of commandline arguments are : ",len(sys.argv))
    print("Datatype of argv is : ",type(sys.argv))
    print("First commandline argument is : ", sys.argv[0])
    print("Second commandline argument is : ", sys.argv[1])
    print("Third commandline argument is : ", sys.argv[2])
    print("Forth commandline argument is : ", sys.argv[3])


if __name__ == "__main__":
    main()