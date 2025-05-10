# Calculate cube of number using lambda function

def CalculateCube(No):
    # return No * No * No
    return No ** 3

Result = CalculateCube(8)
print("Using regular function")
print("Cube is : ",Result)

#

CalculateCube = lambda No : No**3

ret = CalculateCube(8)
print("\nUsing lambda function")
print("Cube is : ",ret)