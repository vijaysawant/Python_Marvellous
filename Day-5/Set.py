# Set in python

# Syntax is {}
# Not Heterogenious
# Unordered
# Not indexed
# Not allowed duplicate data
# set is mutable but data is immutable

data = {10, 90.67, "Hello", True, 10}
print("Datatype is : ",type(data))
print("Length is : ",len(data))
print(data)

print("\nCan't access by data/element by index")
# print(data[0])

print("\nSet is unorded, ")
data.add(3)
print(data)
data.remove(10)

print("\nData using loop :")
for value in data:
    print(value)