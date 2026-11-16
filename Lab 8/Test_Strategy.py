from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Order import Order
from BulkDiscount import BulkDiscount
from PercentageDiscount import PercentageDiscount
from StudentDiscount import StudentDiscount


supplier = Supplier("S001", "Tech Supplies", "sales@example.com")
product = PhysicalProduct("P001", "Desk Lamp", 25.0, 20, 1.0, supplier)

order = Order("O001")
order.add_order_line(product, 10)

print(f"No discount total: ${order.calculate_total():.2f}")

order.set_discount(BulkDiscount(200, 20))
print(f"Bulk discount total: ${order.calculate_total():.2f}")

order.set_discount(PercentageDiscount(10))
print(f"Percentage discount total: ${order.calculate_total():.2f}")

order.set_discount(StudentDiscount())
print(f"Student discount total: ${order.calculate_total():.2f}")

shared_discount = PercentageDiscount(10)

order_a = Order("O002", shared_discount)
order_b = Order("O003", shared_discount)

print(f"Both orders share the same strategy: {order_a.discount is order_b.discount}")
