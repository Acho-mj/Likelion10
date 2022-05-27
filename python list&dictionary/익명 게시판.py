#방법 1_질문과 답변이 무엇인지 알 수 있음
total_list = []     #아무것도 없는 리스트 생성

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})
        #하나의 딕션너리를 만든 후 리스트에 추가하는 방식임

for i in total_list:
    print(i["질문"])    #딕션너리에서 질문을 key로 하여 접근
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)

#방법 2_질문과 답변을 생략함
total_dictionary = {}       #아무것도 없는 딕션너리 생성

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""  #key로 질문이 들어감

for i in total_dictionary:
    print(i)        #질문 하나하나가 i에 저장되고, 이를 출력함
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer        #key 값에 해당하는 value
print(total_dictionary)