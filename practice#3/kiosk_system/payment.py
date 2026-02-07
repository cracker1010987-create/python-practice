def pay(price, money):
    if money >= price:
        return money - price
    else:
        return -1