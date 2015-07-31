# coding: UTF-8
import urllib2
import cookielib
handler=urllib2.HTTPCookieProcessor(cookie)
from lxml import html
url="http://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action="
headers={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
req = urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
ihtml=response.read()
#page = ihtml.decode('gbk')
tree = html.fromstring(ihtml)
children = list(tree[1])
# print children[7][2][4].text
# print children[7][1][1][1].tail
#Movie=[]
#Movie.append((children[1][0][1].text, children[1][1][1][1].tail, children[1][2][1].text))
#print(Movie[0][0],Movie[0][1],Movie[0][2])
print children
