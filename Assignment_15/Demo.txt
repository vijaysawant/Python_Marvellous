"""
2. WAP which accept file name from user and open that file and display the contents of that file on screen.

Input: Demo.txt
Display contents of Demo.txt on console.
"""
import os

def main():
    print("Program to display file content on the screen")
    fileName = input("Enter file name: ")
    isExists = os.path.exists(path=fileName)        # os.path.exists returns True or False
    if isExists:
        print("File exists in current directory")
    else:
        curDirAbsPath = os.path.abspath(os.path.curdir)
        print(f"File does not exists in current directory '{curDirAbsPath}/'")       

if __name__ == "__main__":
    main()