#Shopping Basket Class - www.101computing.net/shopping-basket-class/
from Item import Item
from ShoppingBasket import ShoppingBasket

tomatoSoup = Item("Tomato Soup","200mL can", 0.70)
spaghetti = Item("Spaghetti","500g pack", 1.10)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10)
mozarella = Item("Mozarella","100g", 1.50)
gratedCheese = Item("Grated Cheese","100g",2.20)

myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)

myBasket.view()