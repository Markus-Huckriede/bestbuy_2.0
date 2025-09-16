from products import Product

class Store:
    def __init__(self, products: list[Product]):
        self.products = products


    def add_product(self, product: Product) -> None:
        self.products.append(product)


    def remove_product(self, product: Product) -> None:
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)


    def get_all_products(self) -> list[Product]:
        return self.products


    def order(self, shopping_list) -> float:
       total_price = 0
       if len(shopping_list) == 0:
           raise ValueError("basket empty")
       for product, quantity in shopping_list:
            total_price += product.buy(quantity)
       return total_price


def start(store: Store):
    while True:
        print("Store Menue")
        print("-----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number (1-4): ")

        if choice == "1":
            all_products = store.get_all_products()
            for index, product in enumerate(all_products, start=1):
                print(f"{index}. {product.show()}")

        elif choice == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")

        elif choice == "3":
            all_products = store.get_all_products()
            shopping_list = []
            print("------")
            for i, product in enumerate(all_products, start=1):
                print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")

            while True:
                product_input = input("When you want to finish order, enter empty text.\nWhich product # do you want? ")
                if product_input == "":
                    break
                try:
                    product_index = int(product_input) - 1
                    amount_input = input("What amount do you want? ")
                    amount = int(amount_input)
                    shopping_list.append((all_products[product_index], amount))
                    print("Product added to list!\n")
                except (ValueError, IndexError):
                    print("Invalid input, try again.")

            try:
                total = store.order(shopping_list)
                print(f"Order complete! Total price: ${total}")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")