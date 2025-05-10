"""
This program is to demonstrate CommandLine Argument concept.
"""
import sys

def main():
    print("Number of commandline arguments are : ",len(sys.argv))
    
    print("List of commandline arguments are : ")
    # for loop
    print("\nUsing for loop")
    for argument in sys.argv:
        print("Argument : ",argument)


    # while loop
    print("\nUsing while loop")
    i = len(sys.argv)
    j = 0
    while(j < i):
        print("Argument : ",sys.argv[j])
        j = j + 1

if __name__ == "__main__":
    main()