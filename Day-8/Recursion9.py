#  Input : 4
# Outpu : 10   (4+3+2+1)

def Add(num):
    sum = 0
    while(num):
        sum = sum + num
        num = num - 1
    return sum

def main():
    res = Add(4)
    print(res)

if __name__ == "__main__":
    main()