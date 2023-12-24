from abc import ABC
from Classes.actor import Actor
from Interfaces.i_return_order import iReturnOrder

class OrdinaryClient(Actor, iReturnOrder):
    def __init__(self, name: str):
        super().__init__(name)


    def isTakeOrder(self):
        return super().getTakeOrder()

    def setTakeOrder(self, takenOrder):
        super().setTakeOrder(takenOrder)

    def isMakeOrder(self):
        return super().getMakeOrder()

    def setMakeOrder(self, makeOrder):
        super().setMakeOrder(makeOrder)

    def getActor(self):
        return self.getName()

    def getName(self):
        return super().getName()

    def setName(self, name):
        super().name = name