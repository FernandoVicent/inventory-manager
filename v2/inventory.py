import datetime
from product import Product
from producer import Producer


class Inventory:
    def __init__(self):
        self.products = []
        self.producers = {}
        self.next_id = 1
        self.log_file = 'logs.txt'


    def log(self, message: str):
        with open(self.log_file, 'a') as file:
            file.write(f"[{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {message}\n")


    def add_producer(self, name:str):
        if name in self.products:
            print("Producer Already exists.")
            return
        self.producers[name] = Producer(name)
        self.log(f"Producer Created {name}")
        print(f"Producer {name} created successfully")


    def add_product(self, name: str, producer_name:str,price:float, quantity:int):
        if producer_name not in self.producers:
            print("Producer not found. Please create it first.")
            return
        product_id = self.next_id
        self.next_id += 1

        product = Product(
            id = product_id,
            name = name,
            producer = self.producers[producer_name],
            price = price,
            quantity = quantity,
        )
        self.products.append(product)
        self.log(f"Product added to inventory {product}")
        print(f"Product {product.name}")


    def find_by_id(self, product_id: int):
        return next((p for p in self.products if p.id == product_id), None)


    def find_by_name(self, name: str):
        return [n for n in self.products if name.lower() in n.name.lower()]


    def find_by_producer(self, producer_name: str):
        return [p for p in self.products if producer_name.lower() in p.producer.name.lower()]


    def show_all(self):
        if not self.products:
            print("No products added to inventory")
        else:
            for p in self.products:
                print(p)


    def update_product(self,product_id: int, **kwargs):
        product = self.find_by_id(product_id)
        if product:
            for key, value in kwargs.items():
                if hasattr(product, key):
                    old_value = getattr(product, key)
                    setattr(product, key, value)
                    self.log(f"{key} changed of {old_value} to {value} in product {product.id}")
        else:
            self.log(f"Product {product.id} not found")


    def remove_product(self, prodcut_id: int):
        product = self.find_by_id(prodcut_id)
        if product:
            self.products.remove(product)
            self.log(f"Product removed from inventory: {product}")
        else:
            self.log(f"Product not found: {prodcut_id}")