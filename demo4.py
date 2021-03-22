# coding: UTF-8 
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import feedparser
import xlwt


def main():
    print("START")
    baseurl = "http://www.qqgexingqianming.com/qinglv/"
    datalist = getData(baseurl)
    savepath = "个性签名.xls"
    saveData(datalist,savepath)

findWord = re.compile(r'<li><p>(.*?)</p></li>',re.S)    #创建正则表达式对象，表示规则


def getData(baseurl):
    datalist = []
    for i in range(1,21):
        url = baseurl + str(i) + str(".htm")
        #print(url)
        html = askURL(url)
        #print(html)
        
        soup = BeautifulSoup(html,"html.parser")
        for boxleft in soup.find_all('div',class_="boxleft"):
            data = []
            boxleft = str(boxleft)
            
            #tag = re.findall(findTag,boxleft)
            #data.append(tag)
            
            word = re.findall(findWord,boxleft)[0]  #通过正则表达式查找指定的字符串
            
            word = re.sub('<p>'," ",word)
            word = re.sub('</p>'," ",word)
            #word = re.sub('<li>'," ",word)
            #word = re.sub('</li>'," ",word)
            
            data.append(word)
            
            #print(data)
            #print(type(data))
        datalist.append(data)
        #print(datalist)
       
    
    return datalist
    


def askURL(url):
    head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    #用户代理，告诉服务器我们是谁
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLerror as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def saveData(datalist,savepath):
    print("Saving...")
    book = xlwt.Workbook()
    sheet = book.add_sheet('sign')

    for i in range(0,20):
        sheet.write(i,0,datalist[i])
   
            
    book.save(savepath)
    



#if __name__ == "__main__":
    
main()
print("OK")
