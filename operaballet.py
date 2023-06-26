import http.client

conn = http.client.HTTPSConnection("www.operaballet.nl")

headers = {
    'cookie': "CookieConsent=%7Bstamp%3A%5E%25%5E27w1Su5z0B8xjxI8ribBBB5ToT3rwhbBfz5zVUfoZVZjdaV%2BnGT8zG0Q%3D%3D%5E%25%5E27%5E%25%5E2Cnecessary%3Atrue%5E%25%5E2Cpreferences%3Atrue%5E%25%5E2Cstatistics%3Atrue%5E%25%5E2Cmarketing%3Atrue%5E%25%5E2Cmethod%3A%5E%25%5E27explicit%5E%25%5E27%5E%25%5E2Cver%3A1%5E%25%5E2Cutc%3A1686913479294%5E%25%5E2Cregion%3A%5E%25%5E27nl%5E%25%5E27%7D; _gcl_au=1.1.1803546389.1686913479; APPID=naob-app-p02",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    'Accept-Language': "nl,en-US;q=0.7,en;q=0.3",
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': "https://www.operaballet.nl/",
    'DNT': "1",
    'Connection': "keep-alive",
    'Upgrade-Insecure-Requests': "1",
    'Sec-Fetch-Dest': "document",
    'Sec-Fetch-Mode': "navigate",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-User': "?1",
    'Sec-GPC': "1",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache"
    }

conn.request("GET", "/over-ons/publicaties", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
