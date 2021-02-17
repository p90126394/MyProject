import urllib.request as req
url="http://www.4pppc.gov.tw/4pppc/?page_id=11056 "
request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
 })
with req.urlopen(request) as response:
    data=response.read()
#print(data)
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find("div",class_="entry-content-inner")
#for title in titles:
 #   if title.a != None:       
print(titles)