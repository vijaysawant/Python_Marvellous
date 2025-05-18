#  Input : 4
# Outpu : * * * *

def Display(no):
    i = 0
    while(i != no):
        print("*", end=" ")
        i = i + 1
    else:
        print("Test")
    print()

def main():
    Display(4)

if __name__ == "__main__":
    main()