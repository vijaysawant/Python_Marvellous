import os
import sys
import time


def DirectoryWatcher(DirectoryName, extension):

    flag = os.path.isabs(DirectoryName)     # check path is absolute path or not
    # if directory path is not absolute path then convert it into absolute path
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)  # Convert path to absolute path

    flag = os.path.exists(DirectoryName)
    # if Directory path does not exists then exit from code
    if flag == False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    # if directory is not a directory then exit from code
    if flag == False:
        print("Path is valid but target is not directory")
        exit()


    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            # fname = os.path.join(FolderName,fname)
            if fname.endswith(extension):
                print(fname)

def main():
    Border = "-"*50
    print(Border)
    print("---------- Marvellous Automation ----------")
    print(Border)
    print()

    if len(sys.argv) == 2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This application is used to perform Directory cleaning")
            print("This is the directory automation script")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory ExpectedExtension")
            print("Please provide valid absolute path")

    elif len(sys.argv) == 3:
            DirectoryWatcher(sys.argv[1], sys.argv[2])
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