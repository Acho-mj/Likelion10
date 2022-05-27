import random
import time     #time.sleep 사용하기 위해 모듈 불러옴

drink = ["아메리카노", "녹차라떼", "오렌지주스", "바닐라라떼"]  #리스트 만들기

while True:     #무한 반복
    print(drink)
    item = input("음료를 추가 해주세요 : ")     #input 함수로 리스트에 추가할 음료 적기
    if(item == "q"):        #q 입력할 경우 무한 반복문 탈출
        break
    else:
        drink.append(item)      #append로 리스트에 추가하기
print(drink)

set_drink = set(drink)      #리스트를 집합으로
while True:
    print(set_drink)
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_drink = set_drink - set([item])     #원래 리스트에서 원하는 항목 삭제하기

print(set_drink, "중에서 선택합니다.")
print("5")
time.sleep(1)       #1초 쉰다
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_drink)))       #랜덤으로 해당 리스트에서 선택하기
