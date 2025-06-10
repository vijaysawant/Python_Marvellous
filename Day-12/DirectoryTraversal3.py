# This program is to travel "Marvellous" directory, here we just put main logic in seperate function
import os

def DirectoryWatcher(DirectoryName):
    for FolerName, SubFolderNames, FileNames in os.walk(DirectoryName):
        print("FolerName : ",FolerName)

        for subf in SubFolderNames:
            print("Sub Folder names : ",subf)

        for fname in FileNames:
            print("File Name : ",fname)

def main():
    print("Enter name of directory that you want to travel : ")
    DirName = input()
    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()