from dataclasses import dataclass
from producer import Producer

@dataclass
class Product:
    id: int
    name: str
    producer: Producer
    price: float
    quantity: int
