# This program is to travel "Marvellous" directory
import os

def main():
    for FolerName, SubFolderNames, FileNames in os.walk("Marvellous"):
        print("FolerName : ",FolerName)

        for subf in SubFolderNames:
            print("Sub Folder names : ",subf)

        for fname in FileNames:
            print("File Name : ",fname)

if __name__ == "__main__":
    main()