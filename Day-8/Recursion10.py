#  Input : 4
# Outpu : 10   (4+3+2+1)

sum = 0
def Add(num):
    global sum
    if(num):
        sum = sum + num
        num = num - 1
        Add(num)
    return sum

def main():
    res = Add(4)
    print(res)

if __name__ == "__main__":
    main()