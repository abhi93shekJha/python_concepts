import buy_item
# import shopping.more_shopping.place_order (this is also one way to import)
from shopping.more_shopping import place_order as p

if __name__=="__main__":
    buy_item.buy_items_from_cart()
    buy_item.multiply(2, 3)
    p.make_order(["Rice"])