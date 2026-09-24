
def get_valid_input():
    entry = input("Enter stock item quantity or type 'quit' to ")

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

def generate_report(total_units, failed_attempts):
    print("Total inventory:", total_units)
    print("Failed entries:", failed_attempts)

inventory = 0 
failed_entries = 0
deliveries_processed = 0

while True:
    entry = get_valid_input()

    if entry == "quit": break
    
    if entry is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, entry)

    tax = calculate_tax(entry)

    print(f"Current inventory: {inventory}")
    print(f"Tax for this entry: {tax}")

    if inventory > 500:
        print("Stock limit exceeded!")
        break

generate_report(inventory, failed_entries)




