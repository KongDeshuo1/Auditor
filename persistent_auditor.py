INVENTORY_FILE = "inventory.txt"
FIRST_ORDER_ID = 1001


def load_inventory():
    """Read the saved total and order history from inventory.txt.
    If the file doesn't exist, start with an empty inventory."""
    total = 0
    history = []  # each item: (order_id, product_name, quantity)

    try:
        with open(INVENTORY_FILE, "r") as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        return total, history

    if lines and lines[0].strip().isdigit():
        total = int(lines[0].strip())

    for line in lines[1:]:
        parts = line.split(",")
        if len(parts) < 3:
            continue
        order_id = parts[0].strip()
        quantity = parts[-1].strip()
        name = ",".join(parts[1:-1]).strip()
        if order_id.isdigit() and quantity.isdigit():
            history.append((int(order_id), name, int(quantity)))

    return total, history


def save_inventory(total, history):
    """Write the total (line 1), then one order per line: id,name,quantity."""
    with open(INVENTORY_FILE, "w") as file:
        file.write(str(total) + "\n")
        for order_id, name, quantity in history:
            file.write(f"{order_id},{name},{quantity}\n")


def get_product_name():
    name = input("Enter Product Name (or type 'quit' to quit): ").strip()

    if name == "quit":
        return "quit"

    if name == "":
        print("Invalid entry. Product name cannot be empty.")
        return None

    return name


def get_valid_input():
    entry = input("Enter Quantity: ")

    if entry == "quit":
        return "quit"

    if not entry.isdigit():
        print("Invalid entry. Please enter a valid quantity.")
        return None

    return int(entry)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate


def show_orders(history):
    print("Current Orders:\n")
    for order_id, name, quantity in history:
        print(f"{order_id}, {name}, {quantity}")
    print()


def generate_report(total_units, failed_attempts):
    print("Total inventory:", total_units)
    print("Failed entries:", failed_attempts)


inventory, history = load_inventory()
failed_entries = 0

show_orders(history)

while True:
    name = get_product_name()

    if name == "quit":
        break

    if name is None:
        failed_entries += 1
        continue

    entry = get_valid_input()

    if entry == "quit":
        break

    if entry is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, entry)

    if history:
        order_id = max(item[0] for item in history) + 1
    else:
        order_id = FIRST_ORDER_ID
    history.append((order_id, name, entry))

    tax = calculate_tax(entry)

    print("\nNew Order Added:")
    print(f"{order_id},{name},{entry}")
    print(f"Current inventory: {inventory}")
    print(f"Tax for this entry: {tax}\n")

    if inventory > 500:
        print("Stock limit exceeded!")
        break

save_inventory(inventory, history)
print(f"\nOrder successfully saved to {INVENTORY_FILE}")
generate_report(inventory, failed_entries)