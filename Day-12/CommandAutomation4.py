# This script is a template to interact with user.
import sys

def main():
    Border = "-"*50
    print(Border)
    print("---------- Marvellous Automation ----------")
    print(Border)
    print()

    if len(sys.argv) == 2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This application is used to perform ----")
            print("This is the automation script")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py <Argument1> <Argument2>")

        else:
            print("Use the given flags as :")
            print("--h : Use to display the help")
            print("--u : Use to display the usage")
    else:
        print("Warning: Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Use to display the help")
        print("--u : Use to display the usage")

    print()
    print(Border)
    print("------- Thank you for using script -------")
    print("--------- Marvellous Infosystems ---------")
    print(Border)


if __name__ == "__main__":
    main()