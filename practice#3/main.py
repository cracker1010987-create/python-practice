from kiosk_system import menu, payment
all_menus = menu.get_menus()
for name,price in all_menus.items():
    print(f" - {name}: {price}원")
order = input("주문하실 메뉴를 입력하세요: ")
order_price = menu.get_price(order)
 
if order_price is None:
    print("없는 메뉴입니다.")
    
else:
    print(f"[{order}]를 선택하셨습니다. 가격은 {order_price}원 입니다.")

    money = int(input("돈을 넣어주세요: "))

    result = payment.pay(order_price, money)

    if result >= 0:
        print(f"결제 완료! 거스름돈 {result}원을 받아가세요.")
    else:
        print("잔액이 부족합니다. 결제가 취소됩니다.")
