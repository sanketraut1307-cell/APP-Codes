class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Product Inventory")
        print("------------------")

        for p in self.products:
            print("Product ID:", p.product_id)
            print("Product Name:", p.name)
            print("Price:", p.price)
            print("Category:", p.category())
            print("------------------")


# Create inventory
inventory = Inventory()

# Add products
inventory.add_product(Product(101, "Laptop", 55000))
inventory.add_product(Product(102, "Keyboard", 800))
inventory.add_product(Product(103, "Headphones", 1500))

# Display all products
inventory.display_products()

# Output - 
# Product Inventory
# ------------------
# Product ID: 101
# Product Name: Laptop
# Price: 55000
# Category: Expensive
# ------------------
# Product ID: 102
# Product Name: Keyboard
# Price: 800
# Category: Affordable
# ------------------
# Product ID: 103
# Product Name: Headphones
# Price: 1500
# Category: Expensive
# ------------------
