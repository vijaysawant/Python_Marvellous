# Tuple in python:

# Syntax is ()
# Heterogenious
# Ordered - displays data in the order in which data stored
# Indexed
# data is immutable
# tuple is immutable
# tuple allowed duplicate element

data = (10, "Hello", 90.67, True, 10)

print("Data type is : ", type(data))
print("Length is : ",len(data))
print(data)

print("\nData tuple is ordered and is indexed")
print("0th index value : ", data[0])
print("1st index value : ", data[1])

# data[0] = 11
# print("\nFist element changed : ", data[0])     # cann't change data / element of tuple


print("\nData display using for loop :")
for value in data:
    print(value)
print("\nData display using for loop index :")
for i in range(len(data)):
    print(data[i])