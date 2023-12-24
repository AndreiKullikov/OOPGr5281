from Classes.actor import Actor
from Interfaces.i_return_order import iReturnOrder

class PromotionLimitExceededError(Exception):
    pass

class PromotionClient(Actor, iReturnOrder):
    # Атрибуты акции 
    promotion_name = "Новогоднии Скидки"  # Название акции
    client_id = 1  # id клиента 
    max_participants = 100  # количество участников 
    current_participants = 99  
    
    def __init__(self, name: str):
        super().__init__(name)

    def getPromotionDetails(self):
        # Доступ к атрибутам
        return {
            "Название Акции": PromotionClient.promotion_name,
            "ID клиента": PromotionClient.client_id,
            "количество участников акции ": PromotionClient.current_participants
        }

    def getActor(self):
        return super().getName()
#Присоединение к акции и подсчет количества участников
    def joinPromotion(self):
        if PromotionClient.current_participants < PromotionClient.max_participants:
            PromotionClient.current_participants += 1
            print(f"{self.getName()} воспользовался акцией.")
            return True
        else:
            raise PromotionLimitExceededError("Количество участников акции привышено. отказано в обслуживании.")

