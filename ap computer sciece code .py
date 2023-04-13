class ClothingItem:
    def __init__(self, name, category, color, size, price):
        self.name = name
        self.category = category
        self.color = color
        self.size = size
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def check_item(self, item):
        if item in self.items:
            return True
        else:
            return False

    def total_cost(self):
        return sum([item.price for item in self.items])

    def checkout(self):
        print("Your shopping cart contains the following items:")
        for item in self.items:
            print(f"{item.name}, {item.category}, {item.color}, {item.size}, ${item.price}")
        print(f"Total cost: ${self.total_cost()}")

        confirm = input("Confirm checkout? (y/n): ")
        if confirm.lower() == "y":
            self.items = []
            print("Thank you for shopping!")

def filter_items(items, category):
    return list(filter(lambda x: x.category == category, items))

def search_items(items, query):
    return list(filter(lambda x: query in x.name or query in x.category or query in x.color or query in x.size, items))

def remove_item(items, item):
    items.remove(item)
    return items

clothing_items = [
    ClothingItem("T-Shirt", "Shirts", "Red", "L", 20.00),
    ClothingItem("Jeans", "Pants", "Blue", "M", 30.00),
    ClothingItem("Sweater", "Sweaters", "Green", "S", 25.00),
    ClothingItem("Jacket", "Outerwear", "Black", "M", 50.00),
    ClothingItem("Skirt", "Dresses", "Yellow", "S", 35.00)
]

cart = ShoppingCart()

while True:
    print("Welcome to our clothing store!")
    print("Please select an option:")
    print("1. View all items")
    print("2. Filter items by category")
    print("3. Search for items")
    print("4. View shopping cart")
    print("5. Add item to cart")
    print("6. Remove item from cart")
    print("7. Checkout")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        for item in clothing_items:
            print(f"{item.name}, {item.category}, {item.color}, {item.size}, ${item.price}")

    elif choice == "2":
        category = input("Enter category: ")
        filtered_items = filter_items(clothing_items, category)
        for item in filtered_items:
            print(f"{item.name}, {item.category}, {item.color}, {item.size}, ${item.price}")

    elif choice == "3":
        query = input("Enter search query: ")
        search_results = search_items(clothing_items, query)
        for item in search_results:
            print(f"{item.name}, {item.category}, {item.color}, {item.size}, ${item.price}")

    elif choice == "4":
        cart.checkout()

    elif choice == "5":
        item_name = input("Enter item name: ")
        item = next((x for x in clothing_items if x.name == item_name), None)
        if item:
            cart.add_item(item)
            print(f"{item.name} added to cart.")
        else:
            print("Item not found.")

    elif choice == "6":
        item_name = input("Enter item name: ")
        item = next((x for x in cart.items if x.name == item_name), None)
        if item:
            cart.remove_item(item)
            print(f"{item.name} removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == "7":
        cart.checkout()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
