import http.client

conn = http.client.HTTPSConnection("www.operaballet.nl")

headers = {
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
    'Cache-Control': "no-cache",
    'TE': "trailers"
    }

conn.request("GET", "/over-ons/publicaties", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
