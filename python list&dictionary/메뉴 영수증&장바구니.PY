import datetime
now = datetime.datetime.now()
nowDate = now.strftime('%H:%M:%S') 
sum_D = 0
sum_B = 0


dessert = {"치즈 케이크":7000, "초코 케이크":7000, "블루베리 케이크":8000, "녹차 케이크":7500, "딸기 케이크":8000 }
beverage = {"아이스 아메리카노":3000, "복숭아 아이스티":4000, "청포도 에이드":4500, "오레오 초코":5000, "요거트 스무디":5500 }
print("디저트 류 => ", dessert)
print("음료 => ", beverage)

menu_D = []
menu_B = []

while True:
    choose_D = input("장바구니에 담고 싶은 디저트 1개를 선택해주세요 : ")
    if choose_D == "q":
        print("장바구니에 담긴 디저트를 알려드립니다.\n", menu_D)
        print("장바구니에 담긴 음료를 알려드립니다.\n", menu_B, "\n\n")
        break
    else:
        menu_D.append(choose_D)
        print(menu_D, "메뉴가 장바구니에 담겼습니다.")
        
    
    choose_B= input("장바구니에 담고 싶은 음료 1개를 선택해주세요 : ")
    if choose_B == "q":
        print("장바구니에 담긴 디저트를 알려드립니다.\n", menu_D)
        print("장바구니에 담긴 음료를 알려드립니다.\n", menu_B, "\n\n")
        break
    else:
        menu_B.append(choose_B)
        print(menu_B, "메뉴가 장바구니에 담겼습니다.")
    

set_D = set(menu_D)     
set_B = set(menu_B)

while True:
    item = input("장바구니에서 삭제하고 싶은 메뉴 1개를 입력해주세요 : ")
    
    if(item == "q"):
        print("최종 장바구니에 담긴 내역을 알려드립니다\n", "디저트: ", set_D, "음료: ", set_B)
        break
    else:
        set_D = set_D - set([item])
        set_B = set_B - set([item])
        print("===현재 장바구니 현황입니다.===", set_D, set_B, "\n\n")  


print("==============영수증을 출력해드리겠습니다===============")
print("주문 시각: ", nowDate)
print("주문 내역: ", set_D | set_B)

for i in list(set_D):
    sum_D += dessert[i]
    
for j in list(set_B):
    sum_B += beverage[j]

sum=sum_D + sum_B
print("주문하신 메뉴의 총 금액은", sum, "원입니다.")
