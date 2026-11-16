from Inventory import Inventory
from Supplier import Supplier
from csv_loader import load_products


inventory = Inventory()
supplier = Supplier("S001", "Tech Supplies", "sales@example.com")

load_products("products.csv", inventory, supplier)