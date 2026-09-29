import json
import os
from pathlib import Path

INVENTORY_FILE = Path(os.environ.get("INVENTORY_FILE", Path(__file__).with_name("inventory.txt")))


def get_valid_input():
    entry = input("Enter stock item quantity or type 'quit' to quit: ").strip()

    if entry.lower() == "quit":
        return "quit"

    if not entry.isdigit():
        print("Invalid entry. Please enter a whole-number quantity.")
        return None

    return int(entry)


def load_inventory(file_path=INVENTORY_FILE):
    """Load the saved total and transaction history, or start with empty data."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        total = saved_data["total"]
        transactions = saved_data["transactions"]
        if not isinstance(total, int) or not isinstance(transactions, list):
            raise ValueError("Inventory file has an unexpected format.")
        if not all(isinstance(amount, int) for amount in transactions):
            raise ValueError("Transaction history has an unexpected format.")
        return total, transactions

    except FileNotFoundError:
        return 0, []
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not read saved inventory ({error}). Starting with an empty inventory.")
        return 0, []


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate


def save_inventory(total_units, transaction_history, file_path=INVENTORY_FILE):
    """Write the total and every valid transaction to the inventory file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    saved_data = {
        "total": total_units,
        "transactions": transaction_history,
    }
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(saved_data, file, indent=4)


def generate_report(total_units, failed_attempts, transaction_history):
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

        if entry == "quit":
            save_inventory(inventory, transaction_history)
            print("Inventory and transaction history saved.")
            break

        if entry is None:
            failed_entries += 1
            continue

        inventory = process_delivery(inventory, entry)
        transaction_history.append(entry)

        print(f"Current inventory: {inventory}")
        print(f"Tax for this entry: {calculate_tax(entry):.2f}")

        if inventory > 500:
            print("Stock limit exceeded!")
            save_inventory(inventory, transaction_history)
            print("Inventory and transaction history saved.")
            break

    generate_report(inventory, failed_entries, transaction_history)


if __name__ == "__main__":
    main()




