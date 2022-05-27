import requests
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

keyword = input("검색어를 입력해주세요: ")
page = int(input("가져올 페이지 숫자를 입력해주세요: "))
print("크롤링할 페이지: " ,page, "페이지")

url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + keyword + "&start=" + str(page)
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }

soup = requests.get(url, headers=headers)
html = BeautifulSoup(soup.text, "html.parser")

results = html.select("li div.news_area > a")
data=[]
n = 0
for key in results:
    n+=1
    print(str(n) + ": " + key.text)
    data.append(key.text)
    if( n >= 10):
        break

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["번호", "제목"])
num = 0
for i in results:
    num +=1
    title = i.text
    sheet.append([num, title])
    
wb.save("new.xlsx")

