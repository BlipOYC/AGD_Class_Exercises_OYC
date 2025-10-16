import pytest
from Items import Item
from ShoppingBasket import ShoppingBasket

@pytest.fixture
def setup_items_and_basket():
    # Create items
    tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, 20)
    spaghetti = Item("Spaghetti", "500g pack", 1.10, 20)
    blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, 20)
    mozarella = Item("Mozarella", "100g", 1.50, 20)
    gratedCheese = Item("Grated Cheese", "100g", 2.20, 29)

    # Create basket and add items
    basket = ShoppingBasket()
    basket.addItem(tomatoSoup, 4)
    basket.addItem(blackOlives, 1)
    basket.addItem(mozarella, 2)
    basket.addItem(tomatoSoup, 6)

    return basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese

def test_shopping_basket_setup(setup_items_and_basket):
    """Checking that the basket is initialized"""
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese = setup_items_and_basket
    assert basket.items == {tomatoSoup: 10, blackOlives: 1, mozarella: 2}


def test_add_normal(setup_items_and_basket):
    """Test basket.addItem() works"""
    basket, *_, blackOlives, mozarella, gratedCheese = setup_items_and_basket
    basket.addItem(gratedCheese, 20)
    basket.addItem(blackOlives, 2)
    basket.addItem(mozarella, 12)
    assert basket.items[gratedCheese] == 20
    assert basket.items[blackOlives] == 3
    assert basket.items[mozarella] == 14

    #Adding the maximum possible

    basket.addItem(gratedCheese, 9)
    assert basket.items[gratedCheese] == 29

def test_more_than_stock(setup_items_and_basket):
    basket, tomatoSoup, *_ = setup_items_and_basket
    basket.addItem(tomatoSoup, 142857) #Nice number
    assert basket.items[tomatoSoup] == 20

def test_non_positive_add(setup_items_and_basket):
    basket, tomatoSoup, *_ = setup_items_and_basket
    with pytest.raises(ValueError):
        basket.addItem(tomatoSoup, 0)

    with pytest.raises(ValueError):
        basket.addItem(tomatoSoup, -123)

def test_remove_normal(setup_items_and_basket):
    basket, tomatoSoup, *_ = setup_items_and_basket
    basket.removeItem(tomatoSoup, 3)
    assert basket.items[tomatoSoup] == 7
    basket.removeItem(tomatoSoup) #In here as it is expected/normal behaviour
    with pytest.raises(KeyError):
        basket.items[tomatoSoup] #Perfect, tomatoSoup has been deleted from the dict, hence check by KeyError

def test_remove_edge(setup_items_and_basket):
    basket, tomatoSoup, spaghetti, blackOlives, *_ = setup_items_and_basket
    basket.removeItem(tomatoSoup, 11) #More than available
    basket.removeItem(blackOlives, -2)
    with pytest.raises(KeyError): #Similar to above
        basket.items[tomatoSoup]
    with pytest.raises(KeyError):
        basket.items[blackOlives]
    with pytest.raises(ValueError): #Spaghetti was not added
        basket.removeItem(spaghetti, 4)

def test_update(setup_items_and_basket):
    basket, tomatoSoup, *_ = setup_items_and_basket
    basket.updateItem(tomatoSoup, 2)
    assert basket.items[tomatoSoup] == 2
    assert tomatoSoup.stock_level == 18

    basket.updateItem(tomatoSoup, 20)
    assert basket.items[tomatoSoup] == 20
    assert tomatoSoup.stock_level == 0

def test_update_edge(setup_items_and_basket):
    basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese = setup_items_and_basket
    valids = [tomatoSoup, blackOlives, mozarella]
    invalids = [spaghetti, gratedCheese]
    for invalid in invalids:
        with pytest.raises(ValueError):
            basket.updateItem(invalid, invalid.stock_level - 1) #So we know the issue isn't because of stock level
    for valid in valids:
        basket.updateItem(valid, 0)
        with pytest.raises(KeyError): #Again, testing for absence
            basket.items[valid]

def test_reset(setup_items_and_basket):
    basket, *items = setup_items_and_basket
    for item in items:
        basket.addItem(item, item.stock_level) #Max it out (by this point, we can be reasonably sure addItem works)
    basket.reset()
    assert basket.items == {}
