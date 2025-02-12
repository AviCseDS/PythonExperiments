class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Stock: {self.stock}"

products = {}

def main():
    while True:
        print("\n1. Add a new Product")
        print("2. Update the stock of an existing Product")
        print("3. Display the Product Details")
        print("4. Exit the program")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            products[name] = Product(name, price, stock)
            print("Product added successfully")

        elif choice == "2":
            name = input("Enter product name to update: ")
            if name in products:
                quantity = int(input("Enter quantity to add/remove: "))
                products[name].update_stock(quantity)
                print("Stock updated successfully")
            else:
                print("Product not found.")

        elif choice == "3":
            name = input("Enter product name: ")
            if name in products:
                print(products[name])
            else:
                print("Product not found.")

        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

# Uncomment the following line to run the program (but be aware that input will not be interactive in Jupyter)
main()
