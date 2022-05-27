from random import *

name = input("\n당신의 이름은?: ")
print("\n===== 안녕하세요, %s님 당신은 집순이일까요? =====" %name)
print("===== 모든 질문의 대답을 네 또는 아니오로 답변해주세요 =====")
num = int(input(" 받을 질문의 개수를 입력해주세요(최대 7개 가능): "))

qna = {"집 밖에 나가는 것 자체가 스케줄인가요?":"","불금에는 북적대는 곳보단 집인가요?":""
     ,"휴대폰만 있어도 심심하지 않은가요?":"", "카톡, 문자 알림을 잘 확인하지 않나요?":""
     ,"'아무 생각이 없다. 왜냐하면 아무생각이 없기 때문이다'라고 자주 느끼나요?":""
     ,"당신은 배달앱 VIP인가요?":""
     ,"친구와의 약속이 갑작스레 파토났을 때 아쉽다는 생각보다 '오예!'라는 생각이 더 자주 드나요?":""}

Q = sample(list(qna), num)  #중복 제외
ans = {}
for i in range(0, num):
    print("{0}".format(Q[i]), end=" ")
    answer = input(": ")
    ans[i] = answer

list_ans = list(ans.values())
list_num = len(list_ans)
list_yes = 0
for i in range(0, list_num):
    if(len(list_ans[i]) == 1):
        list_yes += 1

percent = ( list_yes / list_num ) * 100
if(percent >= 75):
    print("\n당신은 집순이입니다")
elif(percent >= 50):
    print("\n당신은 집을 더 좋아하네요")
elif(percent >= 25):
    print("\n당신은 밖을 더 좋아하네요")
else:
    print("\n당신은 바깥순이입니다")
