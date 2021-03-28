# coding : UTF-8 #
from lxml import etree
import requests
from lxml.html import fromstring,tostring
from html.parser import HTMLParser
from lxml import html
import re
import json

print("START")
url = "http://www.qqgexingqianming.com"
#head = {"user agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}


response = requests.get(url)
response.encoding = 'utf-8'

#print(response.text)

tree = etree.HTML(response.text)

#print(tree)

result = tree.xpath('//div[@class="hd-tab"]/a/text()') 


#print(result)

urllist = []
taglist = []

for i in range(0,39):
    tag = result[i]
    taglist.append(tag)  
#print(taglist)
  
result1 = tree.xpath('//div[@class="hd-tab"]/a/@href')

for j in range(0,39):
    baseurl = url + str(result1[j])
    urllist.append(baseurl)
#print(urllist)


for o in range(0,39):

    tag1 = taglist[o]

    url1 = urllist[o]
    url2 = url1 + str(2) + str(".htm")
        
       
    
    while True:        
        response1 = requests.get(url2)
        response1.encoding = 'utf-8'

        
        tree1 = etree.HTML(response1.text)
        result2 = tree1.xpath('//div[@class = "boxleft"]/ul[@class = "list"]/li/p/text()')
             
        result3 = tree1.xpath('//div[@class = "page"]/a/@href')

        
        if len(result3) == 7:
            break
    
        url2 = url + str(result3[7])
        #print("第"+str(result3[7])+"页")
    
        dic = {"tag" :tag1,"content" : result2}
        #print(dic)
                    
        dic1 = json.dumps(dic,ensure_ascii = False)
        #print(dic1)

        filename = "b.json"
        with open(filename,'a',encoding = 'utf-8') as file_obj:
            file_obj.write(dic1)
            file_obj.write("\n")

print("OK")
            
        
    
        
