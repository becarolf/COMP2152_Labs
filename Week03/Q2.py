#Q2 - Shopping Cart (Lists - Searching and Removal)

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
print(f"Number of apples: {cart.count("apple")} ")
print(f"Position of milk: {cart.index("milk")} ")
cart.remove("apple")
print(f"Removed item using pop: {cart.pop()} ")
print(f"Is banana in the cart?", "banana" in cart)
print(f"Final cart: {cart} ")
