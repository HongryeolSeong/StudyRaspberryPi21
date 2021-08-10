from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

url = 'https://search.naver.com/search.naver?query=날씨'
html = req.get(url)
#pprint(html.text)
soup = bs(html.text, 'html.parser')

datas = soup.find('div', {'class':'detail_box'})
#pprint(finedust)

details = datas.findAll('dd')
#print(details)

# 미세먼지
finedust = details[0].find('span', {'class', 'num'}).get_text()
# 초미세먼지
ultrafinedust = details[1].find('span', {'class', 'num'}).get_text()
# 오존지수
ozone = details[2].find('span', {'class', 'num'}).get_text()
# 출력
print('{0}, {1}, {2}'.format(finedust, ultrafinedust, ozone))