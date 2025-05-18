# This program is to find recurssion limit 

import sys

def main():
    print("Recurssion limit : ",sys.getrecursionlimit())
    sys.setrecursionlimit(2000)
    print("Recurssion limit : ",sys.getrecursionlimit())

if __name__ == "__main__":
    main()