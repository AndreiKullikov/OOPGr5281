import sys


from typing import List
from Domain.bottle import Bottle
from Domain.product import Product
from Services.coin_dispenser import CoinDispenser
from Services.display import Display
from Services.holder import Holder
from Services.vending_machine import VendingMachine



if __name__ == "__main__":
    
    assort: List[Product] = []
    item1 = Product(100, 1, "Lays")
    item2 = Product(50, 2, "Cola")
    item3 = Bottle(150, 3, "Mineral Water", 101, 1.5)
    assort.append(item1)
    assort.append(item2)
    assort.append(item3)


    hold1 = Holder(4, 4)
    coinDesp = CoinDispenser(0)
    disp = Display()

    venMachine = VendingMachine(hold1, coinDesp, assort, disp)

    for prod in venMachine.getProducts():
        print(prod)


