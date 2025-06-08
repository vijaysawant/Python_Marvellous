# create file in exclusive mode.

def main():
    print("Enter the name of file that you want to create : ")
    FileName = input()  # demo.txt

    fobj = open(FileName, "x")
    fobj.close()
if __name__ == "__main__":
    main()