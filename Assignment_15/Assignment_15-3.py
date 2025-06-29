"""
3. WAP which accept file name from user and create new file named as Demo.txt and copy all content from
existing file into new file. Accept file name through command line argumemnts.

Input: ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
"""
import os
import sys
def copyFileContent(existingFile, newFile="Demo.txt"):
    oldFileHandler = open(existingFile, 'r')
    newFileHandler = open(newFile, 'w')

    oldData = oldFileHandler.read()
    newFileHandler.write(oldData)
    


def main():
    # $>python Assignment-15-3.py existingFile.txt
    if len(sys.argv) == 2:
        if sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This program is use to copy contents from existing file into new file")
            print("Use given options")
            print("--u or --U : Use to display the usage")
        elif sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this script")
            print("$python <ProgramName.py> <existingFileName>")
            print("Use given options")
            print("--h or --H : Use to display the help")
        else:
            # print("Use given options")
            # print("--h or --H : Use to display the help")
            # print("--u or --U : Use to display the usage")
            
            existingFileName = sys.argv[1]
            # check file exist or not
            if not os.path.exists(path=existingFileName):
                print(f"ERROR - File '{existingFileName}' not present in current directory")
    
            copyFileContent(existingFile=existingFileName, newFile="Demo.txt")

    else:
        print("Warning: Invalid number of command line arguments")
        print("Use the given options as :")
        print("--h or --H : Use to display the help")
        print("--u or --U : Use to display the usage")
    
   
if __name__ == "__main__":
    main()