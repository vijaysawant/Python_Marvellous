"""
1. WAP which accepts file name from user and check whether that file exists in current directory or not.

Input: Demo.txt
Check whether Demo.txt exists or not.
"""
import os

def main():
    print("Program to check existance of file in the current directory")
    fileName = input("Enter file name: ")
    isExists = os.path.exists(path=fileName)        # os.path.exists returns True or False
    if isExists:
        print("File exists in current directory")
    else:
        print("File does not exists in current directory")

if __name__ == "__main__":
    main()