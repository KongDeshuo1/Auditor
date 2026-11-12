from abc import ABC, abstractmethod
from Supplier import Supplier


class Product(ABC):
    
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def display_supplier(self) -> None:
        self.__supplier.display_information()
    
    def get_product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            print("Invalid quantity. Stock cannot be negative.")
            return

        self.__stock = quantity

    def get_price(self) -> float:
        return self.__price

    def display_information(self) -> None:
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def to_dict(self) -> dict[str, str | float | int | dict[str, str]]:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }
