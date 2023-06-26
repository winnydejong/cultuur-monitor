import requests
from bs4 import BeautifulSoup
import re

cookies = {
    'CookieConsent': '{stamp:^%^27w1Su5z0B8xjxI8ribBBB5ToT3rwhbBfz5zVUfoZVZjdaV+nGT8zG0Q==^%^27^%^2Cnecessary:true^%^2Cpreferences:true^%^2Cstatistics:true^%^2Cmarketing:true^%^2Cmethod:^%^27explicit^%^27^%^2Cver:1^%^2Cutc:1686913479294^%^2Cregion:^%^27nl^%^27}',
    '_gcl_au': '1.1.1803546389.1686913479',
    'APPID': 'naob-app-p02',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'nl,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.operaballet.nl/',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'CookieConsent={stamp:^%^27w1Su5z0B8xjxI8ribBBB5ToT3rwhbBfz5zVUfoZVZjdaV+nGT8zG0Q==^%^27^%^2Cnecessary:true^%^2Cpreferences:true^%^2Cstatistics:true^%^2Cmarketing:true^%^2Cmethod:^%^27explicit^%^27^%^2Cver:1^%^2Cutc:1686913479294^%^2Cregion:^%^27nl^%^27}; _gcl_au=1.1.1803546389.1686913479; APPID=naob-app-p02',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

r = requests.get('https://www.operaballet.nl/over-ons/publicaties', cookies=cookies, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
urls = soup.findAll('a', href=True)

res = []

for u in urls:
    if re.match(r'.*aarverslag.*', u['href']):
        res.append('https://www.operaballet.nl' + u['href'])
    else:
        pass

# open file in write mode
with open(r'operaballet.txt', 'w') as fp:
    for r in res:
        # write each item on a new line
        fp.write("%s\n" % r)
fp.close()
