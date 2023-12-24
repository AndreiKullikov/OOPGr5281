import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.products = []
        self.cash_balance = 0

    def add_product(self, product):
        self.products.append(product)

    def insert_cash(self, amount):
        self.cash_balance += amount

    def buy_product(self, product_index):
        if 0 <= product_index < len(self.products):
            product = self.products[product_index]
            if self.cash_balance >= product.price:
                self.cash_balance -= product.price
                del self.products[product_index]
                return f"Successfully bought {product.name}"
            else:
                return "Not enough funds to buy the product"
        else:
            return "Invalid product index"

class VendingMachineInterface(QWidget):
    def __init__(self, vending_machine):
        super().__init__()

        self.vending_machine = vending_machine

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Product List
        self.product_list = QListWidget()
        self.update_product_list()
        layout.addWidget(self.product_list)

        # Cash Input
        cash_layout = QHBoxLayout()
        cash_layout.addWidget(QLabel("Cash Input:"))
        self.cash_input = QLineEdit()
        cash_layout.addWidget(self.cash_input)
        layout.addLayout(cash_layout)

        # Buy Product Button
        buy_button = QPushButton("Buy Product")
        buy_button.clicked.connect(self.buy_product)
        layout.addWidget(buy_button)

        self.setLayout(layout)
        self.setWindowTitle("Vending Machine")

    def update_product_list(self):
        self.product_list.clear()
        for product in self.vending_machine.products:
            item = QListWidgetItem(f"{product.name} - ${product.price}")
            self.product_list.addItem(item)

    def buy_product(self):
        cash_amount = self.cash_input.text()
        try:
            cash_amount = float(cash_amount)
            self.vending_machine.insert_cash(cash_amount)
            selected_item = self.product_list.currentItem()
            if selected_item:
                product_index = self.product_list.row(selected_item)
                result = self.vending_machine.buy_product(product_index)
                self.update_product_list()
                print(result)
        except ValueError:
            print("Invalid cash input. Please enter a valid number.")

if __name__ == '__main__':
    vending_machine = VendingMachine()
    vending_machine.add_product(Product("Soda", 1.5))
    vending_machine.add_product(Product("Chips", 2.0))
    vending_machine.add_product(Product("Candy", 1.0))

    app = QApplication(sys.argv)
    interface = VendingMachineInterface(vending_machine)
    interface.show()
    sys.exit(app.exec_())