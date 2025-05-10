# Calculate power of number using regular function, shorter way

def Power(X, Y):
    return X**Y

Ret = Power(10, 7)
print("Using regular function")
print("Result is : ", Ret)

####

Pwr = lambda X,Y : X**Y
print("\nUsing lambda function")
Ret = Pwr(10, 7)
print("Result is : ", Ret)