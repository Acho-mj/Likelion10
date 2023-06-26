from tkinter import *
from tkinter import messagebox
import webbrowser
import requests
from bs4 import BeautifulSoup

#확인, 취소 버튼 있는 메세지 박스
def clickSearch():
    response = messagebox.askokcancel("검색 확인/취소", keyword.get() + ", 검색하시겠습니까?")
    if(response == 1):
        crawling()      #확인버튼 누르면 crawling 함수 실행
    else:
        win.destroy()   #취소버튼 누르면 윈도우 창 꺼짐

#네이버 뉴스 기사 검색
def crawling():
     
    #해킹 목적이 아님을 나타내기 위해 정보 알림
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }

    for i in range(1, 5):  #크롤링할 페이지 수를 1에서 4로 제한
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query="+ keyword.get() + "&start=" + str(i)

        #url의 html에서 해당 css 선택자를 가진 부분 선택
        soup = requests.get(url, headers=headers)
        html = BeautifulSoup(soup.text, "html.parser")
        results = html.select("li div.news_area > a")
    
        n = 0
        for key in results:
            n+=1
            print(str(n) + ": " + key.text)     #크롤링이 되는지 콘솔창으로 확인하기 위함
            print(key.get('href'))      #크롤링이 되는지 콘솔창으로 확인하기 위함
            resultnews.append(key.text) #리스트에 뉴스 기사 제목 추가
            resulturl.append(key.get('href'))   #리스트에 뉴스 기사 url 추가
    
    #크롤링한 뉴스 기사 제목을 리스트박스에 추가        
    for i in range(len(resultnews)):
        listbox.insert(i, str(i+1) + '번 : ' + resultnews[i])  
    
def openUrl(event):
    i = event.widget.curselection()[0]  #리스트박스에서 선택된 항목의 인덱스 값 반환
    webbrowser.open_new(resulturl[i])   #선택한 기사의 웹 브라우저로 이동

#윈도우창
win =Tk()
win.title("원하는 뉴스 기사 확인하기")
win.geometry("550x500")
win.resizable(False, False) #크기 변하지 않음


global listbox, resultnews, resulturl   #전역 변수 설정
     
resultnews = [] #뉴스 기사 제목 리스트 생성
resulturl = []  #뉴스 기사 url 리스트 생성

#검색어 레이블
upper = Label(win)
upper.pack(fill = "both", padx = 20, pady = 5)
inputKeyword = Label(upper, text="검색어를 입력하세요 : " ,bg="lightgreen", font="맑은고딕 10")
inputKeyword.pack(side="left")
inputKeyword = StringVar()


#검색어 입력 창
keyword = Entry(upper, width = 30)      
keyword.pack(side="left")


#검색 버튼
click = Button(upper, text ="검색", command=clickSearch)     
click.pack(side="left") 


#스크롤창
scroll = Scrollbar(win, orient='vertical')
listbox = Listbox(win, selectmode='extended', yscrollcommand=scroll.set)
listbox.bind('<Double-Button>', openUrl)
scroll.config(command = listbox.yview)
scroll.pack(side = 'right', fill = Y)
listbox.pack(side= 'left', fill = 'both', expand=True)


win.mainloop()