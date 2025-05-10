# List in python:

# Syntax is []
# Heterogenious
# Ordered - displays data in the order in which data stored
# Indexed
# data mutable
# list is mutable (use of append)
# list allowed duplicate element

data = [10,90.67,"Hello",40, True]

print("Data type is : ", type(data))
print("Length is : ",len(data))
print(data)
print("\nData list is ordered and is indexed")
print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[0] = 11
print("\nFist element changed : ", data[0])

data.append(40)
print(data)

print("\nData display using for loop :")
for value in data:
    print(value)