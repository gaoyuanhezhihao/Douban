# coding: UTF-8

import spynner
import pyquery
import time
import BeautifulSoup
from lxml import html
browser = spynner.Browser()
browser.create_webview()
browser.set_html_parser(pyquery.PyQuery)
browser.load("http://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=")
browser.load_jquery(True)
try:
    browser.wait_load(10)
except:
    pass

ihtml = browser.html
#page = ihtml.decode('utf-8')
tree = html.fromstring(ihtml)
browser.close()
print tree[1][4][0][1][0][6][0][0][1][0][0][0].text
