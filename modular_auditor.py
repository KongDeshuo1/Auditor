inventory = 0 
failed_entries = 0

print("Inventory Management System")
print("Enter stock item quantity, or type 'quit' to exit.")

while True:
    entry = input("Enter stock item quantity: ")

    if entry.lower() == "quit":
        break

    if not entry.isdigit():
        print("Invalid entry. Please enter a valid quantity.")
        failed_entries += 1
        continue

    quantity = int(entry)

    if quantity < 0:
        print("Please input a positive number.")
        failed_entries += 1
        continue
    inventory += quantity

    print(f"Current inventory: {inventory}")

    if inventory > 500:
        print("Stock limit exceeded!")
        break
    else:
        pass

print("Total inventory:", inventory)
print("Failed entries:", failed_entries)




