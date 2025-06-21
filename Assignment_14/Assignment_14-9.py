"""
9. Create a class Product with attributes name and price. Implement __eq__ method to comapare two products
if they are equal in price.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, value):
        if isinstance(value, Product):
            print("Both objects are of same class")
        else:
            print("Both objects are not of same class")
        
        return (self.name == value.name and self.price == value.price)

def main():
    product_name_1 = input("Enter 1st product name: ")
    product_name_2 = input("Enter 2nd product name: ")
    product_price_1 = int(input("Enter 1st product price: "))
    product_price_2 = int(input("Enter 2nd product price: "))

    product_1 = Product(name=product_name_1, price=product_price_1)
    product_2 = Product(name=product_name_2, price=product_price_2)
    if product_1 == product_2:
        print("Both products are same")
    else:
        print("Both products are not same")

if __name__ == "__main__":
    main()