# -*- coding:utf-8 -*-
#!/usr/bin/python
# Filename: test.py
# 糗事百科 爬虫

import urllib2
import urllib
import re
 
def QSBK(page):
    page = pageNum
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<h2>(.*?)</h2>(.*?)</a>.*?<div class="content">(.*?)</div>(.*?)<div.*?stats">(.*?)<span.*?stats-vote">(.*?)<i.*?number">(.*?)</i>',re.S)
        items = re.findall(pattern,content)
        # print items
        for item in items:
            print u'标题:'+item[0]
            print u'内容:'+item[2]
            print item[6] + u'好笑'
            print '===================================================================================================================='
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

pageNum = int(raw_input(u'input the pageNum:\n'))
QSBK(pageNum)