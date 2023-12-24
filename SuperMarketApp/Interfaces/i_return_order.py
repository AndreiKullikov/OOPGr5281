from abc import ABC, abstractmethod

class iReturnOrder(ABC):
    @abstractmethod
    def initiateReturn(self, order_id: int) -> bool:
        pass

    @abstractmethod
    def processReturn(self, order_id: int) -> str:
        pass


        # Реализация абстрактных методов iReturnOrder 

    def initiateReturn(self, order_id: int) -> bool:
        # Логика инициирования возврата
        print(f"запрос возврата заказа {order_id} от клиента: {self.getName()} .")
        return True  

    def processReturn(self, order_id: int) -> str:
        # Логика обработки возврата
        print(f"возврат для заказа {order_id} от клиента: {self.getName()} .")
        return "возврат произведен успешно" 