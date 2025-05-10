ChkEO = lambda N : N % 2 == 0

print(ChkEO(12))


def ChkEvenOdd(Number):
    if(Number % 2 == 0):
        return True
    return False

ret = ChkEvenOdd(10)
if ret == True:
    print("Even")
else:
    print("False")