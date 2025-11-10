from inventory import Inventory


def menu(options):
    print("\n======= INVENTORY MENU =======")
    for i, opt in enumerate(options, start=1):
        print(opt)
    try:
        return int(input("\nSelect an option: "))
    except ValueError:
        print("Invalid input.")
        return -1


def main():
    inventory = Inventory()

    while True:
        option = menu([
            "[1] Create Producer",
            "[2] Create Product",
            "[3] Show All Products",
            "[4] Find Product",
            "[5] Update Product",
            "[6] Delete Product",
            "[7] Show Logs",
            "[0] Exit"
        ])

        if option == 1:
            name = input("Producer name: ")
            inventory.add_producer(name)

        elif option == 2:
            name = input("Product name: ")
            producer_name = input("Producer name: ")
            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                inventory.add_product(name, producer_name, price, quantity)
            except ValueError:
                print(" Invalid numeric value.")

        elif option == 3:
            inventory.show_all()

        elif option == 4:
            search = input("Search by ID, name or producer: ")
            if search.isdigit():
                product = inventory.find_by_id(int(search))
                print(product if product else "Product not found.")
            else:
                results = inventory.find_by_name(search) or inventory.find_by_producer(search)
                if results:
                    for p in results:
                        print(p)
                else:
                    print("No products found.")

        elif option == 5:
            try:
                product_id = int(input("Enter product ID to update: "))
                product = inventory.find_by_id(product_id)
                if not product:
                    print("Product not found.")
                    continue

                print(f"Leave empty to keep current values.")
                new_name = input(f"New name ({product.name}): ") or None
                new_price = input(f"New price ({product.price}): ")
                new_quantity = input(f"New quantity ({product.quantity}): ")

                inventory.update_product(
                    product_id,
                    name=new_name or product.name,
                    price=float(new_price) if new_price else product.price,
                    quantity=int(new_quantity) if new_quantity else product.quantity
                )
            except ValueError:
                print("Invalid value.")

        elif option == 6:
            try:
                product_id = int(input("Enter product ID to delete: "))
                inventory.remove_product(product_id)
            except ValueError:
                print("Invalid ID.")

        elif option == 7:
            try:
                with open(inventory.log_file, "r") as file:
                    print("\n===== SYSTEM LOGS =====")
                    print(file.read())
            except FileNotFoundError:
                print("No logs found.")

        elif option == 0:
            print("Exiting the system...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
