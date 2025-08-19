import requests
import re
rurl ="https://dhlottery.co.kr/gameResult.do?method=byWin"
response = requests.get(rurl)
print("상태코드:",response.status_code)
#<meta id="desc" name="description" content="동행복권 1184회 당첨번호 14,16,23,25,31,37+42. 1등 총 15명, 1인당 당첨금액 1,910,655,600원.">
temptext = re.search(r'<meta\s*id\=\"desc\"\s*name\=\"description\"\s*content\=\"동행복권\s*(.+)회\s*당첨번호\s(.+)\.\s*1등\s*총',\
                     response.text)
print(temptext.group(1))
print(temptext.group(2))
