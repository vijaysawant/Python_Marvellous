
def main():
    print("Enter the name of file that you want to create : ")
    FileName = input()

    fobj = open(FileName, "w")  # Demo.txt

    print("Enter the data that you wnat to write into the file")
    data = input()
    fobj.write(data)
    fobj.close()

if __name__ == "__main__":
    main()