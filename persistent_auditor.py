import json
import os
from pathlib import Path

INVENTORY_FILE = Path(os.environ.get("INVENTORY_FILE", Path(__file__).with_name("inventory.txt")))


def get_valid_input():
    entry = input("Enter stock item quantity or type 'quit' to quit: ")

    if entry == "quit": 
            return "quit"

    if not entry.isdigit():
        print("Invalid entry. Please enter a valid quantity.")
        return None

    
    return int(entry)


def load_inventory(file_path=INVENTORY_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        total = saved_data["total"]
        transactions = saved_data["transactions"]

def save_inventory(total_units, transaction_history, file_path=INVENTORY_FILE):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    saved_data = {
        "total": total_units,
        "transactions": transaction_history,
    }
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(saved_data, file, indent=4)


def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate

def generate_report(total_units, failed_attempts,transaction_history):
    print("Total inventory:", total_units)
    print("Failed entries:", failed_attempts)
    print("Transaction history:", transaction_history)

def main():
    inventory, transaction_history = load_inventory()
    failed_entries = 0

    print(f"Loaded inventory: {inventory}")
    print(f"Previous transactions: {transaction_history}")

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

generate_report(inventory, failed_entries, transaction_history)


if __name__ == "__main__":
    main()




