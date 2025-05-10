"""
This program is to demonstrate CommandLine Argument concept.
"""
import sys

def main():
    print("Number of commandline arguments are : ",len(sys.argv))
    print("List of commandline arguments :")
    # for loop
    print("\nUsing for loop")
    for i in range(1,len(sys.argv)):
        print("Argument : ",sys.argv[i])


    # while loop
    print("\nUsing while loop")
    i = len(sys.argv)
    j = 0
    while(j < i):
        if j == 0:
            j = j + 1
            continue
        else:
            print("Argument : ",sys.argv[j])
            j = j + 1

if __name__ == "__main__":
    main()