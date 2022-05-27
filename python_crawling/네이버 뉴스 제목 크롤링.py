from bs4 import BeautifulSoup
import requests
from datetime import datetime

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# span - item_title
results = soup.select("li div.cluster_text > a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

rank = 1
for result in results:
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1

