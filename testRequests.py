# coding : UTF-8 #
from lxml import etree
import requests
from lxml.html import fromstring,tostring
from html.parser import HTMLParser
from lxml import html
import re
#import feedparser
#import json

url = "http://www.qqgexingqianming.com"
#head = {"user agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}


response = requests.get(url)
response.encoding = 'utf-8'

#print(response.text)
#print(type(response.text))


tree = etree.HTML(response.text)

#print(tree)
#print(type(tree))

result = tree.xpath('//div[@class="hd-tab"]/a/text()')


#print(result)
#print(type(result))
urllist = []
taglist = []
for i in range(0,39):
    tag = result[i]
    #print(tag)
    #print(type(tag))
    taglist.append(tag)
    
print(taglist)
  
result1 = tree.xpath('//div[@class="hd-tab"]/a/@href')

for j in range(0,39):
    #print(j)
    baseurl = url + str(result1[j])
    #print(baseurl)
    
    urllist.append(baseurl)
    
print(urllist)


#抓取页面
for o in range(0,38):
    tag1 = taglist[o]
    print(tag1)
    
    for n in range(0,38):
        url1 = urllist[n]
        url2 = url1 + str(2) + str(".htm")
        
       
    
        while True:        
            response1 = requests.get(url2)
            response1.encoding = 'utf-8'

            #print(response1.text)
        
            tree1 = etree.HTML(response1.text)
            answ = tree1.xpath('//div[@class = "boxleft"]/ul[@class = "list"]/li/p/text()')
    
            #for s in answ:
                #print(s,"\n")
            
             
            result3 = tree1.xpath('//div[@class = "page"]/a/@href')
            print(len(result3))
            #nextpage = str(result3[7])
            if len(result3) == 7:
                break
            #number = re.finall(r'\d',result3[5])
            url2 = url + str(result3[7])
            print("第"+str(result3[7])+"页")
            
            
           
            
        
    
        
        
            
            
    
