from products import Product


class Store:
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.quantity for p in self.products if p.is_active())

    def get_all_products(self) -> list[Product]:
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        if not shopping_list:
            raise ValueError("Shopping basket is empty.")
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def start(store: Store):
    while True:
        print("\nStore Menu")
        print("------------")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number (1-4): ").strip()

        if choice == "1":
            all_products = store.get_all_products()
            if not all_products:
                print("No products available.")
            else:
                print("\nAvailable products:")
                for index, product in enumerate(all_products, start=1):
                    print(f"{index}. {product.show()}")

        elif choice == "2":
            print(f"\nTotal quantity in store: {store.get_total_quantity()}")

        elif choice == "3":
            all_products = store.get_all_products()
            if not all_products:
                print("No products available for order.")
                continue

            print("\n------ Products ------")
            for i, product in enumerate(all_products, start=1):
                print(f"{i}. {product.name} - ${product.price} ({product.quantity} pcs)")
            print("----------------------")

            shopping_list = []
            while True:
                product_input = input("\nEnter product # (or press Enter to finish): ").strip()
                if product_input == "":
                    break
                try:
                    product_index = int(product_input) - 1
                    if not (0 <= product_index < len(all_products)):
                        print("Invalid product number.")
                        continue
                    amount = int(input("Enter quantity: ").strip())
                    if amount <= 0:
                        print("Quantity must be greater than 0.")
                        continue

                    shopping_list.append((all_products[product_index], amount))
                    print("Product added to order!")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            try:
                total = store.order(shopping_list)
                print(f"Order complete! Total price: ${total:.2f}")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")
