from Items import Item


class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items = {}  # A dictionary of all the items in the shopping basket: {item:quantity}
        self.checkout = False

    # A method to add an item to the shopping basket
    def addItem(self, item, quantity=1):
        if quantity <= 0:
            print(f"Invalid operation - Quantity must be a positive number! No {item.name} added.")
            return

        if item.stock_level == 0:
            print(f"No stock left for {item.name}.")
            return

        if quantity > item.stock_level:
            print(f"Not enough of {item.name} to add {quantity}. Adding remaining {item.stock_level} instead.")
            quantity = item.stock_level

        self.items[item] = self.items.get(item, 0) + quantity
        item.stock_level -= quantity

    # A method to remove an item from the shopping basket (or reduce it's quantity)
    def removeItem(self, item, quantity=0):
        #Easier on the eyes
        """Removes an item from the shopping basket."""

        if item not in self.items:
            print(f"{item.name} not in basket.")
            return

        if quantity <= 0 or quantity >= self.items[item]:
            print("Either quantity is smaller or equal to 0 or the quantity entered is more than currently in the basket}")
            print(f"Removing all {item.name} from the basket")
            item.stock_level += self.items[item]
            self.items.pop(item)
        else:
            #Normal
            self.items[item] -= quantity
            item.stock_level += quantity

    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item, quantity):
        if item not in self.items:
            print(f"{item.name} not in basket.")
            return
        if quantity <= 0:
            self.removeItem(item) #Just remove the item
            return
        else:
            self.items[item] = quantity
            return


    # A method to view/list the content of the basket.
    def view(self):
        totalCost = 0
        print("---------------------")
        for item in self.items:
            quantity = self.items[item]

            cost = quantity * item.price
            print(" + " + item.name + " - " + str(quantity) + " x £" + '{0:.2f}'.format(
                item.price) + " = £" + '{0:.2f}'.format(cost))
            totalCost += cost
        print("-------------------------")
        print(" = £" + '{0:.2f}'.format(totalCost))
        print("-------------------------")

        # A method to calculate the total cost of the basket.

    def getTotalCost(self):
        totalCost = 0
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            totalCost += cost
        return totalCost

    def reset(self):
        for item, quantity in self.items.items():
            item.stock_level += quantity
        self.items = {}
