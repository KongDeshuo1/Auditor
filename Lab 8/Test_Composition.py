from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Order import Order


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")
product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)

order_a = Order("O001")
order_b = Order("O002")

order_a.add_order_line(product, 2)
order_b.add_order_line(product, 5)

print("Same OrderLine object?")
print(order_a.order_lines[0] is order_b.order_lines[0])

print(f"Order A total: ${order_a.calculate_total():.2f}")
print(f"Order B total: ${order_b.calculate_total():.2f}")