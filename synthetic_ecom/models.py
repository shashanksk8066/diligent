from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class Customer:
    id: int
    name: str
    email: str

@dataclass
class Order:
    id: int
    customer_id: int
    product_id: int
    quantity: int
