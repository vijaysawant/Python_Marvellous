# Dictionary in python

# Syntax is { key : value }
# Heterogenious
# Ordered
# Indexed - not numberic, access by key
# Key duplicate allowed but old get overwritten *
# Value duplicate allowed 
# Data is mutable (value only)

data = {"Name" : "Let us C", 
        "Author" : "Y Kanetkar", 
        "Price" : 340, 
        "Plubication":"BPB Plublication",
        # "Name" : "Let us C++"     # Key duplicate allowed but old get overwritten *
        }

print("length is : ",len(data))
print("data type : ",type(data))

print(data)
print(data["Author"])

print("\nData is mutable")
data["Price"] = 400
print(data)