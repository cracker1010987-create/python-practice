def get_menus():
    return{"아메리카노":3000, "라떼":3500, "카푸치노": 3700}
def get_price(name):
    menus = get_menus()

    if name in menus:
        return menus[name]
    else:
        return None