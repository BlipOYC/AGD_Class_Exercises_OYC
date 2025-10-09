#Shopping Basket Class - www.101computing.net/shopping-basket-class/
from Items import Item
from ShoppingBasket import ShoppingBasket

tomatoSoup = Item("Tomato Soup","200mL can", 0.70,43)
spaghetti = Item("Spaghetti","500g pack", 1.10,32)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10,10)
mozarella = Item("Mozarella","100g", 1.50,67)
gratedCheese = Item("Grated Cheese","100g",2.20,14)

myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 44)
myBasket.addItem(blackOlives, -1)
myBasket.addItem(mozarella,15)
myBasket.addItem(mozarella, 6)
myBasket.removeItem(mozarella, 7)
myBasket.addItem(tomatoSoup, 4)

myBasket.view()