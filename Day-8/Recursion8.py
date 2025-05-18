# This is actual recursive function example using while loop
#  Input : 4
# Outpu : * * * *

def Display(no):
    if no != 0:
        print("*", end=" ")
        no = no -1
        Display(no)


def main():
    Display(4)

if __name__ == "__main__":
    main()