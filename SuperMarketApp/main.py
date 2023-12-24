from Classes.market import Market
from Classes.ordinary_client import OrdinaryClient
from Classes.special_client import SpecialClient
from Classes.tax_inspector import TaxInspector
from Classes.promo_client import PromotionClient

magnit = Market()

client1 = OrdinaryClient("boris")
client2 = SpecialClient("prezident", 1)
client3 = TaxInspector()
client4 = PromotionClient("Andrew")


# подробности акции
client4.joinPromotion()
promotion_details = client4.getPromotionDetails()
print("Деталии Акции после новго клиента:")
print(promotion_details)
print()

# Возврта заказа
order_id_to_return = 123  
return_initiated = client2.initiateReturn(order_id_to_return)
print(return_initiated)

return_result = client2.processReturn(order_id_to_return)
print(return_result)
print()


magnit.acceptToMarket(client1)
magnit.acceptToMarket(client2)
magnit.acceptToMarket(client3)
magnit.acceptToMarket(client4)

magnit.update()