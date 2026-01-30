#Q2
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple") 
milk_position = cart.index("milk")
print(f"Number of apples:  {apple_count}")
print(f"Position of milk: {milk_position}")
cart.remove("apple") #using remove
removed_item = cart.pop()
print(f"Removed item using pop: {removed_item}")
print("Is banana in cart?" , "banana" in cart)