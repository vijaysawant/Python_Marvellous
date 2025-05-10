# Dictionary in python - Loops 

data = {"Name" : "Let us C", 
        "Author" : "Y Kanetkar", 
        "Price" : 340, 
        "Plubication":"BPB Plublication",
        }
print("Dictionary : ",data)

print("\nLoop to display keys")
for x in data:
    print(x)

print("\nLoop to display values")
for x in data.values():
    print(x)

print("\nLoop to display key and value")
for x,y in data.items():
    print(x,y)