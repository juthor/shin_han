#9. 금융

from bs4 import BeautifulSoup
from pprint import pprint #예쁘게 출력하기 위한 용도
import requests
import re

#웹페이지 열고 소스코드 읽기
html=requests.get("https://www.shinhancard.com/conts/person/card_info/dream/check/finance/index.jsp")
soup=BeautifulSoup(html.text, 'html.parser')
html.close()

#해당 영역 추출하기
data1_list=soup.findAll('div',{'class':'shcd-card-list-item'})
#pprint(data1)
count=0

def no_space(text):
    text1=re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text2=re.sub('\n\n', '', text1)

    return text2

name_list=[]
detail_list=[]
annual_list=[]
count=0
for d in data1_list:
    data2=d.findAll('h4', {'class':'shcd-card-name'})
    data4=d.findAll('div', {'class':'shcd-card-spec'})
    data3=d.findAll('dl', {'class':'shcd-card-annual-fee'})

    name_list.append([t.text for t in data2])
    
    temp=[i.text for i in data3]
    for x in temp:
        xx=x.strip()
        annual_list.append(no_space(xx))
    #annual_list=[x.strip() for x in temp]

    temp=[i.text for i in data4]
    #for y in temp:
     #   x.strip()
      #  detail_list=no_space(xx)
    detail_list=[x.strip() for x in temp]
    count=count+1
    
for i in range(count):
    print(i+1, "번", name_list[i])
    #print(detail_list[i])
    print(annual_list[i])
    
print("\n")
#for a in (detail_list):
