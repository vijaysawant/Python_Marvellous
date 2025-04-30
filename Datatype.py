import sys

no = 11
print("value 0f no is:",no)
print("Datatype of no:",type(no))
print(f"Size of no is: {sys.getsizeof(no)} bytes")

large_no = 12345678901
print("Size of large_no is:{0} bytes",sys.getsizeof(large_no))