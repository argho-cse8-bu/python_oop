class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Marketplace:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def sign_up_customer(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)
        print("Customer sign-up successful!")

    def sign_up_seller(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)
        print("Seller sign-up successful!")

    def login(self, email, password):
        user_found = False
        for customer in self.customers:
            if customer.email == email and customer.password == password:
                print("Customer login successful!")
                user_found = True
                break

        for seller in self.sellers:
            if seller.email == email and seller.password == password:
                print("Seller login successful!")
                user_found = True
                break

        if not user_found:
            print("User not found. Please try again.")

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print("Product added successfully!")

    def display_products(self):
        for i, product in enumerate(self.products):
            print(f"{i+1}. {product.name}")

    def buy_product(self, customer, product_index, quantity):
        product = self.products[product_index - 1]
        if product.quantity >= quantity:
            product.quantity -= quantity
            print(f"You have successfully purchased {quantity} {product.name}(s).")
        else:
            print("Insufficient quantity available for purchase.")

    def run(self):
        while True:
            print("Main Menu:")
            print("1. Sign up as a customer")
            print("2. Sign up as a seller")
            print("3. Login")
            choice = input("Enter your choice: ")

            if choice == "1":
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                self.sign_up_customer(email, password)

            elif choice == "2":
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                self.sign_up_seller(email, password)

            elif choice == "3":
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                self.login(email, password)
                if email in [customer.email for customer in self.customers]:
                    while True:
                        print("Customer Menu:")
                        print("1. Add a product")
                        print("2. Back to main menu")
                        customer_choice = input("Enter your choice: ")
                        if customer_choice == "1":
                            name = input("Enter the product name: ")
                            price = float(input("Enter the product price: "))
                            quantity = int(input("Enter the product quantity: "))
                            self.add_product(name, price, quantity)
                        elif customer_choice == "2":
                            break
                elif email in [seller.email for seller in self.sellers]:
                    while True:
                        print("Seller Menu:")
                        print("1. Buy a product")
                        print("2. Back to main menu")
                        seller_choice = input("Enter your choice: ")
                        if seller_choice == "1":
                            print("Available products:")
                            self.display_products()
                            product_index = int(input("Enter the product number: "))
                            quantity = int(input("Enter the quantity: "))
                            self.buy_product(email, product_index, quantity)
                        elif seller_choice == "2":
                            break
            else:
                print("Invalid choice. Please try again.")


marketplace = Marketplace()
marketplace.run()
