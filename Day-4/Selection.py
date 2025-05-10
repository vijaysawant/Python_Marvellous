MIN_AGE = 18

def main():
    age = int(input("Enter your age : "))
    if age < MIN_AGE:
        print("You can not cast the vote")
    else:
        print("You can cast the vote")

if __name__ == "__main__":
    print("--CHECK AGE FOR VOTE--")
    main()

